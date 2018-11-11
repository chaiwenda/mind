# encoding: utf-8
"""
清空text文件
"""
import sys
def clearText(texturl):
    print(sys._getframe().f_code.co_name)  # 当前函数名
    print(sys._getframe().f_lineno)  # 当前行号
    file = open(texturl,'r+')
    file.truncate()

if __name__ == '__main__':
    clearText('F:\\django_project\\vue\\public\\result2.txt')