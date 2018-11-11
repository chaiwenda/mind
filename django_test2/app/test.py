# from data_deal.textOCR import textOCR
from data_deal.textDeal import textDeal

from data_deal.clearText import clearText

from data_deal.neo4j import neo4jwrite
from data_deal.clearImg import *
from data_deal.clearNeo4j import *
import sys
file_img = 'E:\\django_test2\\vue\public\\image\\172.17.173.51\\'
file_move = 'E:\\django_test2\\vue\public\\image_move\\172.17.173.51\\'
file_result = 'E:\\django_test2\\vue\public\\result\\'
text_in = 'E:\\django_test2\\vue\\public\\result1.txt'
text_out = 'E:\\django_test2\\vue\\public\\result2.txt'
password = '123456'
def clearAll(file_img,file_result,text_in, text_out, password, file_move):
    print(sys._getframe().f_code.co_name)  # 当前函数名
    print(sys._getframe().f_lineno)  # 当前行号
    clearText(text_in)
    clearText(text_out)
    clearNeo4j(password)
    clearFile(file_move)
    clearFile(file_img)
    clearFile(file_result)

def data_project(file_img,file_result,text_in, text_out, password):
    print(sys._getframe().f_code.co_name)  # 当前函数名
    print(sys._getframe().f_lineno)  # 当前行号
    # textOCR(file_img, text_in, file_result)
    textDeal(text_out, text_in)
    neo4jwrite(text_out, password)


import time
time1 = time.clock()
clearAll(file_img,file_result,text_in, text_out, password,file_move)
#data_project(file_img,file_result,text_in, text_out, password)
time2 = time.clock()
print(time2-time1)
