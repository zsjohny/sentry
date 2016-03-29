#coding:utf-8
import post
import re,sys,pcre,msgpack,pygrok,json,os,time,threading
from django.conf import settings
def bom_aware_readline(fileobj):
    atstart = (fileobj.tell() == 0)
    line = ""
    while True:
        l = fileobj.readline()
        if atstart:
            if len(l) > 2 and ord(l[0]) == 239 and ord(l[1]) == 187 and ord(l[2]) == 191:
                # UTF-8 BOM detected: skip it over
                l = l[3:]
            atstart = False
        # if line ends with \, append \n, then to the top of the loop to append the next line.
        if l.rstrip("\r\n").endswith("\\"):
          line += l.rstrip("\r\n")
          line += "\n"
        else:
          line += l
          break
    return line

def bom_aware_readlines(fileobj):
    lines = []
    while True:
        l = bom_aware_readline(fileobj)
        if l:
            lines.append(l)
        else:
            break
    return lines

# reads Sorkins .conf files into a dictionary of dictionaries
def readConfFile(path):
    if not len(path) > 0:
        return None

    settings = {}
    currStanza = None

    if not os.path.exists(path):
      # TODO audit consumers, then remove this file creation entirely, it's
      # deeply wrong.
      confdir = os.path.dirname(path)
      if not os.path.exists(confdir):
        os.makedirs(confdir)
      f = open(path, 'w')
    else:
      f = open(path, 'rb')
      lines = bom_aware_readlines(f)
      settings = readConfLines(lines)

    f.close()
    return settings

# takes a list of lines in conf file format, and splits them into dictionary (of stanzas), each of which is a dictionary of key values.
# the passed list of strings can come either from the simple file open foo in readConfFile, or the snazzier output of popen("btool foo list")
def readConfLines(lines) :
    currStanza = "default"
    settings   = {currStanza : {}}

    # line is of the form key = value where multi-line value is combined by '\n'
    for line in lines:
      l = line.strip()
      if l.startswith("#") : continue
      if l.startswith('['):
          stanza = l.lstrip('[')
          endLoc = stanza.rfind(']')
          if endLoc >= 0:
            stanza = stanza[:endLoc]
          if stanza not in settings:
              settings[stanza] = {}
          currStanza = stanza
      elif line.find("=") > 0:
          # keys are assumed to have no '=' chars in them. Values are allowed to have one or more.
          (key, val) = l.split('=',1)
          key = key.strip()
          val = val.strip()
          if val and val[-1] == "\\":
              # This could be a multi-line value and strip will get rid \n
              # adding back \n to avoid conflating of the 2 settings:
              # SPL-91600
              val = "%s\n" % val
          settings[currStanza][key] = val
    return settings


sourceTypes = readConfFile(settings.MOCK_CONF+'/etc/system/default/props.conf')
transforms = readConfFile(settings.MOCK_CONF+'/etc/transforms.conf')

def spl_match(line='',pattern=''):
	if re.search('(?:\?P\<(.*?)\>|\%\{(.*?)\})',pattern):
		return pygrok.grok_match(line,pattern)
	else:
		m = pcre.search(pattern,line)
		return m.groupdict() if m is not None else None

def pcre_subparse(vl="",l={}):
    pl = re.compile('\[\[(.*?)\]\]')
    ml = pl.findall(vl)
    res = vl
    if len(ml)>0:
        for i in ml:
            sl = i.split(":")
            if len(sl)>1:
                res = vl.replace('[['+i+']]','(?<'+sl[1]+'>'+l[sl[0]]+')')
            else:
                res = vl.replace('[['+i+']]',l[sl[0]])
            vl = res
    return res

def pcre_parse(value="",transforms={}):
    l={}
    for (k,d) in transforms.items():
        if type(d)==dict and d.has_key('REGEX'):
            pa=re.compile('\?\<(.*?)\>')
            v = d['REGEX']
            val = v
            li = pa.findall(v)
            if len(li)>0:
                for i in li:
                    if i == "":
                        val = v.replace('?<>','?:')
                    v=val
                if not v.startswith('(?') or not v.endswith(')'):
                    l[k]='(?:'+v.replace('/','\/')+')'
                else:
                    l[k]=v.replace('/','\/')
            else:
                if not v.startswith('(?') or not v.endswith(')'):
                    l[k]='(?:'+d['REGEX'].replace('/','\/')+')'
                else:
                    l[k]=d['REGEX'].replace('/','\/')
    p = re.compile('\[\[(.*?)\]\]')
    m = p.findall(value)
    result = value
    if len(m)>0:
        result = pcre_subparse(result,l)
        while len(p.findall(result))>0:
        	result = pcre_subparse(result,l)
    else:
        result = pcre_subparse(l[result],l)
        while len(p.findall(result)) > 0:
        	result = pcre_subparse(result,l)
    pp = re.compile('\?\<(.*?)\>')
    mm = pp.findall(result)
    for j in mm:
        count = 0
        for i in mm:
            if j == i:
                count = count + 1
        if count > 1:
            for k in range(count):
                if len(pp.findall(result)) != len(set(pp.findall(result))):
                    result = result.replace(j,j+str(k),k+1)
    return result


# def extract_event(producer,event={}):
def extract_event(event={}):
    '''
    if not has_attr('producer', ctx):
        ctx.producer = KafkaProducer(bootstrap_servers=['kafka','kafka-1'])
    '''
    transforms_stanza = {}
    final_event=event
    for k in sourceTypes[event['sourcetype']].keys():
        if re.search('(?:TRANSFORMS-*|REPORT-*|EXTRACT-*)',k):
            transforms_stanza[k]=transforms['default']
            for (ke,va) in transforms[sourceTypes[event['sourcetype']][k]].items():
                transforms_stanza[k][ke] = va
            transforms_stanza[k]['REGEX']=pcre_parse(sourceTypes[event['sourcetype']][k],transforms)

    for (key,val) in transforms_stanza.items():                       ###############source key################
        if key.startswith('TRANSFORMS'):                     ###############FORMAT###############
            middle_event = spl_match(event['_raw'],val['REGEX'])
        elif key.startswith('REPORT'):
            middle_event = spl_match(event['_raw'],val['REGEX'])
        else:
            middle_event = spl_match(event['_raw'],val['REGEX'])
        if middle_event is None:
            middle_event = event
            middle_event['error'] = 'the part of event can not parse,please check the raw log'
        else:
            for (k,v) in middle_event.items():
                final_event[k] = v
    return final_event
    # producer.producer.send(producer.topic,bytes(json.dumps(final_event)))
    # print final_event


def multilineProcess(object_list,multilineReg,linebreaker,data_dict,producer):
    # multilineReg=r"\[(\d{2})/(\d{2})/(\d{4}) (\d{2}):(\d{2}):(\d{2})\] MW(\d*) P(\d*) PR(\d*)\] (.{5}) - (.*) - (?P<full_message>[\s\S]*?)(?=\r?\n\[\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2}\]|$)"
    #used for content,not line by line
    q=re.compile(multilineReg)

    last_event=""
    last_line_end=False
    number_line_of_a_event=0
    sent_data={}
    for key in data_dict:
        sent_data[key]=data_dict[key]
    for index,line in enumerate(object_list):
        if index==0:
            last_event=line
            continue
        else:
            if q.findall(line):
                last_line_end=True
            if last_line_end:
                sent_data["_raw"]=last_event
                sent_data["linecount"]=number_line_of_a_event+1
                extract_event(producer,sent_data)
                number_line_of_a_event=0
                last_event=line
                last_line_end=False
            else:
                if not re.findall(linebreaker,line):
                    number_line_of_a_event+=1
                last_event=last_event+line

    return True


def break_and_merge_event(filepath,sourcetype,dict_date,producer):
    default_line_breaker=r"([\r\n]+)"
    the_highly_true_sourcetype=sourcetype
    confdict=readConfFile("etc/system/default/props.conf")
    new_sourcetype_conf_set=dict()
    new_sourcetype_conf_set=confdict["default"]
    new_sourcetype_conf_set['sourcetype']=the_highly_true_sourcetype
    new_sourcetype_conf_set.update(confdict[the_highly_true_sourcetype])
    dict_date['sourcetype']=new_sourcetype_conf_set['sourcetype']
    if not new_sourcetype_conf_set.has_key("LINE_BREAKER"):
        new_sourcetype_conf_set["LINE_BREAKER"]=default_line_breaker
    if new_sourcetype_conf_set["LINE_BREAKER"]==default_line_breaker:
        infile=filepath
        if new_sourcetype_conf_set["BREAK_ONLY_BEFORE_DATE"]:
            timestamp = r'(\d+:\d+:\d)'
            stat=multilineProcess(infile,timestamp,default_line_breaker,dict_date,producer)
            return
        if new_sourcetype_conf_set["BREAK_ONLY_BEFORE"]:
            multilineReg=new_sourcetype_conf_set["BREAK_ONLY_BEFORE"]
            stat=multilineProcess(infile,multilineReg,default_line_breaker,dict_date,producer)
            return
    else:
        content_text=filepath
        m=re.split(new_sourcetype_conf_set["LINE_BREAKER"],content_text,maxsplit=0,flags=0)
        if new_sourcetype_conf_set["SHOULD_LINEMERGE"]:
            #do merge
            #判断是用时间戳还是正则做merge
            if new_sourcetype_conf_set["BREAK_ONLY_BEFORE_DATE"]:
                # multilineReg=r"\[(\d{2})/(\d{2})/(\d{4}) (\d{2}):(\d{2}):(\d{2})\] MW(\d*) P(\d*) PR(\d*)\] (.{5}) - (.*) - (?P<full_message>[\s\S]*?)(?=\r?\n\[\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2}\]|$)"
                #timestamp shuod be chosen by sourcetpye,each sourcetype may matchs different timestamp ,but let us first complete the logical process,
                #timestamp = r'(\[\d+/\w+/\d+:\d+:\d+:\d+\s+\+\d+\])'
                timestamp = r'(\d+:\d+:\d)'
                stat=multilineProcess(m,timestamp,new_sourcetype_conf_set["LINE_BREAKER"],dict_date,producer)
                return stat

            if new_sourcetype_conf_set["BREAK_ONLY_BEFORE"]:
                multilineReg=new_sourcetype_conf_set["BREAK_ONLY_BEFORE"]
                stat=multilineProcess(m,multilineReg,new_sourcetype_conf_set["LINE_BREAKER"],dict_date,producer)
                return stat
            if new_sourcetype_conf_set["BREAK_ONLY_AFTER"]:
                pass
        else:
            for line in m:
                sent_data={}
                for key in dict_date:
                    sent_data[key]=dict_date[key]
                if not re.findall(new_sourcetype_conf_set["LINE_BREAKER"],line) and len(line)!=0:
                    sent_data["linecount"]=1
                    sent_data["_raw"]=line
                    extract_event(producer,sent_data)
        producer.producer.close()
        return True
