# encoding: utf-8
"""
查询某一节点名及其子节点构成的子图
返回子图json文件
"""
from py2neo import Graph, Node, Relationship
def makeJson(str_in1, str_time1, str_address1, str_nodeJname1):
    str4 = ''
    def makeJson(str_in, str_time, str_address,str_nodeJname):
        nonlocal str4
        db = Graph("http://localhost:7474/", username="neo4j", password="123456")
        data1 = db.run(
            "match (start)-[]->(n) where start.name='%s'and start.time='%s' return n.name,n.time,n.address,n.nodeJname"
            % (str_in, str_time)).data()
        # data1 = db.run("match (start)-[:Contain]->(n) where ID(start)="+str_in+" return n.name").data()
        str4 = str4 + "{\"name\":\"" + str_in + "\",\"proof\":\"%s\",\"time\":\"%s\",\"nodeJname\":\"%s\"," % (str_address, str_time,str_nodeJname)
        # print(str_address)
        if len(data1) == 0:
            str4 = str4 + "\"children\":[]},"
            return

        if len(data1) > 0:
            str4 = str4 + "\"children\":["
            for i1 in range(len(data1)):
                str1 = data1[i1]['n.name']
                str2 = data1[i1]['n.time']
                str3 = data1[i1]['n.address'].replace("\\", '/')
                str5 = data1[i1]['n.nodeJname']
                makeJson(str1, str2, str3, str5)
        str4 = str4 + "]},"
    makeJson(str_in1, str_time1, str_address1, str_nodeJname1)
    i = 0
    str_out = ''
    str4 = str4.rstrip(',')
    while i < len(str4):
        if str4[i] == ','and (str4[i+1] != '{' and str4[i+1] != '\"'and (str4[i+1] < '0'or str4[i+1] > '9')):
            pass
        else:
            str_out = str_out + str4[i]
        i = i+1
    return "{\"Graph\":{\"tree\":"+str_out+",\"name\":\"开始\"}}"
from data_deal.clearText import clearText
if __name__ == '__main__':
    clearText('E:\\360Downloads\\Vue.D3.tree-master\\data\\data.json')
    file_name = open('E:\\360Downloads\\Vue.D3.tree-master\\data\\data.json', 'w')
    file_name.write(makeJson('开始', '', 'test.jpg', ''))
    print(makeJson('开始', '', '', ''))



