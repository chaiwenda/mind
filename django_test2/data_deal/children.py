# encoding:utf-8
from py2neo import Graph
import json
def children(str_in,password):
    list1 = []
    db = Graph(password=password)
    data1 = db.run("MATCH (n)where n.name=~'.*" + str_in + ".*'  RETURN n.name,n.time").data()
    # data2 = json.dumps(data1)
    for i in data1:
        list1.append({'name': i['n.name'], 'time': i['n.time']})
    return list1

def children2(str_in,str_time,password):
    list1 = []
    db = Graph(password=password)
    data1 = db.run("MATCH (n{name:'" + str_in + "',time:'"+str_time+"'})-[]->(b) return b.name,b.time").data()
    for i in data1:
        list1.append({'name': i['n.name'], 'time': i['n.time']})
    return list1

def children3(str_in,password):
    list1 = []
    db = Graph(password=password)
    data1 = db.run("MATCH (n)where n.name='" + str_in + "'  RETURN n.name,n.time").data()
    # data2 = json.dumps(data1)
    for i in data1:
        list1.append({'name': i['n.name'], 'time': i['n.time']})
    return list1
#children3('华','123456')