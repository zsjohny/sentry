from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from SocketServer import ThreadingMixIn
# from kafka import KafkaProducer
import threading,argparse,re,cgi,sourcetype,json,core,time,datetime


class Buffer_source(object):
    buffer_source_count={}
    buffer_content={}

class LocalsourcetypeMap(object):
    sourctypemap={}

# class Producer(object):
#     kafkas = ['kafka','kafka-1']
#     producer = KafkaProducer(bootstrap_servers=kafkas)
#     topic = ""

buff=Buffer_source()
localmap=LocalsourcetypeMap()
# producer=Producer()


def hand_data(jsondata):
    print " sourcetypemap",localmap.sourctypemap
    if jsondata["source"] in localmap.sourctypemap:
        event=""
        linecount=0
        print "source exsit type",localmap.sourctypemap[jsondata["source"]]
        dict_date={"sourcetype":localmap.sourctypemap[jsondata["source"]],"host":jsondata["host"],"source":jsondata["source"],"_raw":event,"linecount":linecount}
        print "exists sourcetype,per json"

        if '\n' in jsondata["data"]:
            temp=jsondata["data"].split('\n')
            print "this json data %s lines"%(str(len(temp)))
            buff.buffer_content[jsondata["source"]].extend(temp)
        else:
            print "this json data %s line"%(str(1))
            buff.buffer_content[jsondata["source"]].append(jsondata["data"])
        buff.buffer_source_count[jsondata["source"]]+=1

        if buff.buffer_source_count[jsondata["source"]]>=50000:
            print buff.buffer_content[jsondata["source"]]
            stat=core.break_and_merge_event(buff.buffer_content[jsondata["source"]],localmap.sourctypemap[jsondata["source"]],dict_date,producer)
            if stat:
                buff.buffer_content[jsondata["source"]]=[]
            else:
                if buff.buffer_source_count[jsondata["source"]]==100000:
                    #writr buffer data to local file,to void oom
                    buff.buffer_content[jsondata["source"]]=[]
                    print "to void oom ,wirte buffer data %s to local file /tmp/aaa.log"%(str(buff.buffer_source_count[jsondata["source"]]))
    else:
        #buff_data,about 1500 lines. make sure the source the same for 1500 lines,if different start a new buff_data
        if jsondata["source"] in buff.buffer_source_count:
            if '\n' in jsondata["data"]:
                temp=jsondata["data"].split('\n')
                buff.buffer_source_count[jsondata["source"]]+=len(temp)
                buff.buffer_content[jsondata["source"]].extend(temp)
            else:
                buff.buffer_source_count[jsondata["source"]]+=1
                buff.buffer_content[jsondata["source"]].append(jsondata["data"])
        else:
            if '\n' in jsondata["data"]:
                temp=jsondata["data"].split('\n')
                buff.buffer_source_count[jsondata["source"]]=len(temp)
                buff.buffer_content[jsondata["source"]]=temp
            else:
                buff.buffer_source_count[jsondata["source"]]=1
                buff.buffer_content[jsondata["source"]]=[jsondata["data"]]
        for new_source in buff.buffer_source_count:
            buff_content=[]
            if buff.buffer_source_count[new_source]>=1500:
                dict_date={"sourcetype":"","host":jsondata["host"],"source":jsondata["source"],"_raw":"","linecount":0}
                buff_content=buff.buffer_content[new_source]
                newsourcetype=sourcetype.try_to_detect_file_sourcetype(buff_content,new_source)
                if newsourcetype:
                    localmap.sourctypemap[new_source] =newsourcetype
                else:
                    print "can not find the proper sourcetype for the POST DATA!"
                stat=core.break_and_merge_event(buff_content,newsourcetype,dict_date,producer)
                buff.buffer_content[new_source]=[]# after send the buff data ,clean buff
                buff.buffer_source_count[new_source]=0
                print "exists sourcetype,per json come into buffer,stat:",buff.buffer_content

class HTTPRequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        if None != re.search('/senddata/', self.path):
            ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
            if ctype == 'application/json':
                length = int(self.headers.getheader('content-length'))
                data = cgi.parse_qs(self.rfile.read(length), keep_blank_values=1).keys()[0]
                #print type(data),data
                data=json.loads(data)
                stat=hand_data(data)
                self.send_response(200)
                self.end_headers()
                self.wfile.write("ok")
            else:
                data = {}
                self.send_response(200)
                self.end_headers()
                self.wfile.write("debug")
        else:
            self.send_response(403)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write("debug")
        producer.producer.flush()
        return
 
 
class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    allow_reuse_address = True
 
    def shutdown(self):
        self.socket.close()
        HTTPServer.shutdown(self)
 
class SimpleHttpServer():
    def __init__(self, ip, port):
        self.server = ThreadedHTTPServer((ip,port), HTTPRequestHandler)
 
    def start(self):
        self.server_thread = threading.Thread(target=self.server.serve_forever)
        self.server_thread.daemon = True
        self.server_thread.start()
 
    def waitForThread(self):
        self.server_thread.join()
 
    def addRecord(self, recordID, jsonEncodedRecord):
        LocalData.records[recordID] = jsonEncodedRecord
 
    def stop(self):
        self.server.shutdown()
        self.waitForThread()


if __name__=='__main__':

    parser = argparse.ArgumentParser(description='HTTP Server')
    parser.add_argument('port', type=int, help='Listening port for HTTP Server')
    parser.add_argument('ip', help='HTTP Server IP')
    parser.add_argument('topic',help='kafka server topic')
    args = parser.parse_args()
    try:
        print 'start  server!!\n'
        server = SimpleHttpServer(args.ip, args.port)
        producer.topic = args.topic
        server.start()
        server.waitForThread()
    except KeyboardInterrupt:
        print 'Shutting down the server!!'
        server.stop()
    print 'HTTP Server stoped...........'

    '''
python simplewebserver.py 9000 127.0.0.1
POST addrecord example using curl:
curl -XPOST localhost:9000/api/v1/addrecord/1 -d '{"key":"value"}' -H 'Content-Type: application/json'
'''