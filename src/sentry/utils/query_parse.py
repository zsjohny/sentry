# -*- coding: utf-8 -*-
"""
author : wanghe
company: LogInsight
email_ : wangh@loginsight.cn
desc: query parser
"""

import re

querys = [
        "search: (aaa & bbb) | (cc)",
        "search: (aaa & bbb) | (cc)  ; filter: http_methd >=get ; group:sum(rating) by client ; sort:timestamp",
        "search: (CreateEvent | branch)"
]


fields_cmp_pattern = re.compile(r'^(\w+\s*[!=-><]+\s*\w+)+')
field_cmp_pattern = re.compile(r'^(\w+)+\s*([!=-><]+)\s*(\w+)')

search_pattern = re.compile(r'[&|()!]|\w+')

agg_query_pattern = re.compile(r'(\w+)\((\w+)\)')

operator_pri = {'&' : 3, '|' : 2, '!' : 3, '(' : 0, ')' : 1000}


def parse_search_query(q):

    op_st = []
    field_st = []

    items = search_pattern.findall(q.strip())

    for item in items:
        if item in operator_pri:
            if item == '(':
                op_st.append(item)
                pass
            elif item == ')':
                while True:
                    op = op_st.pop()
                    if op == '(':
                        break
                    if op == "!":
                        field_st.append({"not": [field_st.pop()]})
                    elif op == "&":
                        field_st.append({"and": [field_st.pop(), field_st.pop()]})
                    elif op == "|":
                        field_st.append({"or": [field_st.pop(), field_st.pop()]})
                    else:
                        print ":::::::::::::", op
                        return None
                pass
            elif op_st and operator_pri[item] <= operator_pri[op_st[len(op_st) - 1]]:
                while True:
                    op = op_st.pop()
                    if op == "!":
                        field_st.append({"not": [field_st.pop()]})
                    elif op == "&":
                        field_st.append({"and": [field_st.pop(), field_st.pop()]})
                    elif op == "|":
                        field_st.append({"or": [field_st.pop(), field_st.pop()]})
                    else:
                        print ":::::::::::::", op
                        pass
                    if not op_st or operator_pri[item] <= operator_pri[op_st[len(op_st) - 1]]:
                        break
                    pass

                op_st.append(item)

            else:
                op_st.append(item)
                pass
            pass
        else:
            field_st.append(item)
            pass
        pass

    while op_st:
        op = op_st.pop()
        if op == "!":
            field_st.append({"not": [field_st.pop()]})
        elif op == "&":
            field_st.append({"and": [field_st.pop(), field_st.pop()]})
        elif op == "|":
            field_st.append({"or": [field_st.pop(), field_st.pop()]})
        else:
            print ":::::::::::::", op
            return None
        pass
    if len(field_st) <> 1:
        print "parse_search_query error, ", len(field_st)
        return None

    return field_st.pop()


def parse_filter_query(q):

    ret = []
    q = q.strip()

    m = fields_cmp_pattern.match(q)

    if m == None:
        return None

    for item in m.groups():
        m1 = field_cmp_pattern.match(q)
        if m1:
            ret.extend([m1.group(1), m1.group(3), m1.group(2)])
    return ret


def parse_groupby_query(q):

    ret = {}

    items = q.split("by")
    if len(items) == 1:
        ret["by"] = [i.strip() for i in items[0].split(",")]
        return ret

    if len(items) == 2:
        ret["by"] = [i.strip() for i in items[1].strip().split(",")]
        agg_funs = []

        for item in items[0].strip().split(","):
            m = agg_query_pattern.match(item.strip())
            if m:
                agg_funs.append([m.group(2), m.group(1)])

        ret["agg"] = agg_funs
        return ret

    return None


def parse_sort_query(q):
    ret = {}
    items = q.split("\S+")
    if len(items) == 1:
        ret[items[0]] = "asc"
        return ret

    if len(items) % 2 != 0:
        print "parse_sort_query error!"
        return None

    for i in range(0, len(items, 2)):
        ret[items[i]] = items[i+1]

    return ret


def parse_query(q):
    search_query = ""
    filter_query = ""
    groupby_query = ""
    sort_query = ""

    json_query = {}

    for item in q.split(";"):
        pair = item.strip().split(":")

        print "123123123", item

        if len(pair) != 2:
            print "ERROR!"
            continue

        if (pair[0] == "search"):
            search_query = pair[1]
            json_query["search"] = parse_search_query(search_query)
            if json_query["search"] is None:
                return None

        if (pair[0] == "filter"):
            filter_query = pair[1]
            json_query["filter"] = parse_filter_query(filter_query)
            if json_query["filter"] is None:
                return None
            pass

        if (pair[0] == "group"):
            groupby_query = pair[1]
            json_query["group"] = parse_groupby_query(groupby_query)
            if json_query['group'] is None:
                return None
            pass

        if (pair[0] == "sort"):
            sort_query = pair[1]
            json_query["sort"] = parse_sort_query(sort_query)
            if json_query["sort"] is None:
                return None
            pass
        pass

    # return str(json_query).replace("'", "\"")
    return json_query


def test_parse_search():
    querys = [
            "aaa & bb",
            "aaa & bb & cc & dd",
            "aaa | bb | cc | dd",
            "aaa & bb | cc & dd",
            "aaa | bb & cc | dd",
            "(aaa & bb) | cc",
            "aa & (bb | cc)",
            "aa & (bb | cc & dd | ee)",
            "aa & (bb | cc & dd | !ee)"]
    for q in querys:

        r = parse_search_query(q)
        print "====================", q
        print "====================", r
        print "\n"


if __name__ == "__main__":
    test_parse_search()
    for q in querys:
        print '*' * 50
        print "query: ", q
        print "--------------", parse_query(q)
        print "\n"


"""
http://192.168.200.245:8888/tenant/test/CreateEvent/search?q={"search": {"or": ["branch", "CreateEvent"]}}&offset=0&count=6
http://192.168.200.245:8888/tenant/<username>/<index_name>/search?q={"search": {"or": ["branch", "CreateEvent"]}}&offset=0&count=6


http://192.168.200.245:8888/tenant/test/index_test_1/create?schema=key_format=r, value_format=QSQ, columns=(_id, user_id, movie_id, rating)
http://192.168.200.245:8888/tenant/<username>/<index_name>/create?schema=key_format=r, value_format=QSQ, columns=(_id, user_id, movie_id, rating)
"""