# encoding: utf-8
"""
从text写入neo4j
依据节点属性形成的树状图（属性也是链状排列）
"""

from py2neo import Graph, Node, Relationship
import sys
def neo4jwrite(texturl,password):
    print(sys._getframe().f_code.co_name)  # 当前函数名
    print(sys._getframe().f_lineno)  # 当前行号
    file_handle = open(texturl, 'r')
    lines = file_handle.readlines()
    node = []
    edge = []
    last = '*'
    db = Graph("http://localhost:7474/", username="neo4j", password=password)
    first = Node('UserClick', name='开始', time='', address='', pieaddress='', nodeJname='开始')
    db.create(first)
    lastS = Node()
    a = Node()
    b = first
    c = Node()
    d = Node()
    for line in lines:
        print(line, type(line))
        result = line.split("***")
        print(result, len(result))
        nodeId = result[0].strip()
        nodeName = result[1]
        nodeTime = result[2]
        nodeAddress = result[3].strip()
        nodeJname = result[4]
        print('*' + nodeId + '*')
        if nodeId == '输入框节点:':
            lastS = Node('SelectNode', name=nodeName, time=nodeTime, address=nodeAddress, pieaddress='', nodeJname=nodeJname)
            db.create(lastS)
        if nodeId == '用户点击:':
            a = Node('UserClick', name=nodeName, time=nodeTime, address=nodeAddress, pieaddress='', nodeJname=nodeJname)
            db.create(a)
        if nodeId == '公司节点:':
            a = Node('CompanyNode', name=nodeName, time=nodeTime, address=nodeAddress, pieaddress='', nodeJname=nodeJname)
            db.create(a)
        if nodeId == '百度搜索框:':
            a = Node('BaiduNode', name=nodeName, time=nodeTime, address=nodeAddress, pieaddress='', nodeJname=nodeJname)
            db.create(a)
        if nodeId == '输入框节点:':
            relation = Relationship(first, 'Click', lastS)
            db.create(relation)
        if nodeId == '用户点击:':
            relation = Relationship(b, 'ClickList', a)
            db.create(relation)
        if nodeId == '百度搜索框:':
            relation = Relationship(b, 'Baidu', a)
            db.create(relation)
        if nodeId == '公司节点:':
            relation = Relationship(lastS, 'ClickCompany', a)
            db.create(relation)
        b = a
        last = nodeId

if __name__ == '__main__':
    neo4jwrite('F:\\cwd\\mind_test\\django_test2\\vue\public\\result3.txt', "123456")










