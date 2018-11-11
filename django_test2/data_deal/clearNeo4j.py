# encoding: utf-8
"""
清空neo4j数据库
"""
from py2neo import Graph, Node, Relationship
import sys
def clearNeo4j(password):
    print(sys._getframe().f_code.co_name)  # 当前函数名
    print(sys._getframe().f_lineno)  # 当前行号
    db = Graph("http://localhost:7474/", username="neo4j", password=password)
    db.run("match p=()-[]->() delete p")
    db.run("match p=() delete p")

if __name__ == '__main__':
    clearNeo4j("123456")