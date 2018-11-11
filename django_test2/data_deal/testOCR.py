# coding:utf-8
"""
识别用户点击的连通域，进行OCR识别，并对识别结果进行处理，关系的粗略确定
# 百度云ocr账号
nio = ['10792304', 'R2xOMHZhykHekhucL526RctZ', 'ldfAKMLBPXkqgGrQQwjBeK1hF56CwB4C']
x_w = ['10798308', 'nKpoZturaOHjlYGQS9q8HAmU', 'nSGzmGkS7jZ1vGxuiraYEki2ACKtVEXs']
w_d = ['10798308', 'jfPrTkedpNDurbAtkuS7N6D6', '4mGMQrLqNzznKpRPltaw9WqFWCuEOxaG']
y_f = ['10816490', 'KMe18P0lSkaVjp6j4eWKqFp7', 'BP01DVaH4NTP2W2LRPireKRvuEidlOh3']
"""
from PIL import Image
from numpy import *
import cv2
from skimage import measure
from aip import AipOcr
import os
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
from matplotlib.pyplot import *
import shutil

# 文件名分割
def filenamesplit(filename):
    print(sys._getframe().f_code.co_name)  # 当前函数名
    print(sys._getframe().f_lineno)  # 当前行号
    if filename.endswith(".jpg")or filename.endswith(".png"):
        c = filename.split('_')
        time_y = c[1]
        time_m = c[2]
        time_d = c[3]
        time_h = c[4]
        time_m1 = c[5]
        time_s = c[6].split('(')[0]
        a = filename.split('(')[1]
        b = a.split(')')[0]
        x = b.split(',')[0]
        y = b.split(',')[1]
        return int(x), int(y), [time_y, time_m, time_d, time_h, time_m1, time_s]

# 获取文件名列表
def dirsplit(filename):
    dirlist = os.listdir(filename)
    return dirlist


def imfill(im_in):
    print(sys._getframe().f_code.co_name)  # 当前函数名
    print(sys._getframe().f_lineno)  # 当前行号
    size = im_in.shape
    m = size[0]
    n = size[1]
    im_out = zeros([m, n])
    im2, contours, hierarchy = cv2.findContours(im_in, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) != 0 and len(hierarchy) != 0:
        for i in range(len(contours)):
            cv2.drawContours(im_out, contours, i, 255, cv2.FILLED)
    return im_out


def save_img(filename, im_in):
    print(sys._getframe().f_code.co_name)  # 当前函数名
    print(sys._getframe().f_lineno)  # 当前行号
    cv2.imwrite(filename, im_in)


def zonghe(filename_in, mouse_x, mouse_y, filename_out, move_in):
    print(sys._getframe().f_code.co_name)  # 当前函数名
    print(sys._getframe().f_lineno)  # 当前行号
    im1 = cv2.imread(filename_in)
    shutil.move(filename_in, move_in)
    im_out = im1
    print(type(im1))
    im1 = cv2.cvtColor(im1, cv2.COLOR_RGB2GRAY)
    ret, im1 = cv2.threshold(im1, int(255*0.7), 255, cv2.THRESH_BINARY)
    size = im1.shape
    m = size[0]
    n = size[1]
    left1 = int(mouse_x - m / 7)
    right1 = int(mouse_x + m / 7)
    top1 = int(mouse_y - n / 2)  # top1 = 0#top1 = int(mouse_y - n/3)
    bottom1 = int(mouse_y + n / 2)  # bottom1 = n-1#bottom1 = int(mouse_y + n/3)
    if left1 <= 0:
        left1 = 1
    if right1 > m:
        right1 = m - 1
    if top1 <= 0:
        top1 = 1
    if bottom1 > n:
        bottom1 = n - 1
    im3 = Image.fromarray(im1)
    im3 = im3.crop((top1, left1, bottom1, right1))
    im3 = array(im3)
    im1 = im3

    kernel = np.ones((4, 8))
    im1 = cv2.erode(im1, kernel, iterations=1)

    im1 = 255 - im1
    im1 = imfill(im1)
    im1 = uint8(im1)
    im2, contours, hierarchy = cv2.findContours(im1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_KCOS)
    for i in range(len(contours)):
        isb = 0
        x, y, w, h = cv2.boundingRect(contours[i])
        area = cv2.contourArea(contours[i])
        zhoucb = cv2.arcLength(contours[i], True) / (w + h) / 2
        kgb = w / h
        if (mouse_y-top1) >= x and (mouse_y-top1) <= (x + w) and (mouse_x-left1) >= y and (mouse_x-left1) <= (y + h):
            isb = 1
        # print(i, x, y, w, h, area, zhoucb, kgb, isb)
        if isb == 1 and area > 10 and area < 50000 and zhoucb < 1.3 and zhoucb > 0.9 and kgb > 1.8 and kgb < 50:  # if isb[i] == 1 and area > 100 and zhoucb >0.8 and zhoucb<2 and kgb >=2 and kgb < 30:#if isb[i] == 1 and area > 10 and zhoucb < 1.3 and zhoucb > 0.9 and kgb > 5 and kgb < 30:  #if   isb[i]==1 :#if isb[i] == 1 and zhoucb < 1.3 and zhoucb > 0.9 and kgb > 5 and kgb < 30:#if isb[i] == 1 and area < (im1.shape[0] * im1.shape[1])/3:#if isb[i] == 1 and area > 10000 and zhoucb < 1.3 and zhoucb > 0.9 and kgb > 5 and kgb < 30:#if   isb[i]==1 :
            # cv2.drawContours(im3, contours, i, 255, 1)
            # print("yes")
            if (w <= 15 or h <= 15):
                w = w + 15
                h = h + 15
            else:
                w = w
                h = h
            im3 = Image.fromarray(im_out)
            im3 = im3.crop((x+top1, y+left1, x+w+top1, y+h+left1))
            im3 = array(im3)
            save_img(filename_out, im3)
            cv2.rectangle(im_out, (x+top1, y+left1), (x+w+top1, y+h+left1), 255, 2)
            im_out[mouse_x:mouse_x+10,mouse_y:mouse_y+10,0] = 0
            im_out[mouse_x:mouse_x + 10, mouse_y:mouse_y + 10, 1] = 255
            im_out[mouse_x:mouse_x + 10, mouse_y:mouse_y + 10, 2] = 0
            cv2.imwrite(move_in, im_out)
            return im3
        else:
            pass
    im3 = ones((20,20))
    save_img(filename_out, im3)
    cv2.rectangle(im_out, (0 , 0), (20, 20), 255, 2)
    im_out[mouse_x:mouse_x + 10, mouse_y:mouse_y + 10, 0] = 0
    im_out[mouse_x:mouse_x + 10, mouse_y:mouse_y + 10, 1] = 255
    im_out[mouse_x:mouse_x + 10, mouse_y:mouse_y + 10, 2] = 0
    cv2.imwrite(move_in, im_out)
    time.sleep(1)
    return im3


# OCR识别
def OCR(filename):
    print(sys._getframe().f_code.co_name)  # 当前函数名
    print(sys._getframe().f_lineno)  # 当前行号
    #'10792304', 'R2xOMHZhykHekhucL526RctZ', 'ldfAKMLBPXkqgGrQQwjBeK1hF56CwB4C'
    # 'nio = ['10792304', 'R2xOMHZhykHekhucL526RctZ', 'ldfAKMLBPXkqgGrQQwjBeK1hF56CwB4C']
    # x_w = ['10798308', 'nKpoZturaOHjlYGQS9q8HAmU', 'nSGzmGkS7jZ1vGxuiraYEki2ACKtVEXs']
    # w_d = ['10798308', 'jfPrTkedpNDurbAtkuS7N6D6', '4mGMQrLqNzznKpRPltaw9WqFWCuEOxaG']
    # y_f = ['10816490', 'KMe18P0lSkaVjp6j4eWKqFp7', 'BP01DVaH4NTP2W2LRPireKRvuEidlOh3']'
    APP_ID = '11418443'
    API_KEY = 'od6MXy9DvM3TTvHVpIsalgSO'
    SECRET_KEY = '1eoLKrIvpts8oKOysNfDvtK9nVffxCnD'
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    options = {}
    options["detect_direction"] = "true"
    options["probability"] = "true"

    def get_file_content(filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    string = []
    image = get_file_content(filename)
    result = {}
    result = client.basicAccurate(image, options)
    print(result)
    for i in range(len(result['words_result'])):
        string.append(result["words_result"][i]["words"])
    return string

# 节点过滤系统
def node_name_filter(node_name):
    file_filter_path = '../Filter/filter_file2.txt'
    filter_lists = []
    with open(file_filter_path, 'r') as f:
        for line_msg in f:
            filter_lists.append(line_msg.strip('\n').strip(' '))
    for filter_list in filter_lists:
            if filter_list.strip(" ") == node_name.strip(" "):
                return True
    return False


def textDeal(text_in,text_out):
    file = open(text_out, 'r')
    file_in = open(text_in, 'a+')
    lines = file.readlines()
    line_lastcom = "*"
    line_last = '*'
    for line in lines:
        lineStr = line.split('***')
        line_a = lineStr[0]
        line_b = lineStr[1].rstrip()
        # line_b = node_name_filter(line_b)
        # print(line_b)
        line_c = lineStr[2].strip()
        line_d = 'image/pic'+lineStr[3].strip().split('pic')[1]
        if (line_b.endswith('公司') or line_b.endswith('酒店') or line_b.endswith('工厂')) and (
                line_lastcom not in line_b and line_lastcom != line_b):
            line_lastcom = line_b
            if len(line_b) > 9:
                line_e = line_b[0:9] + "..."
            else:
                line_e = line_b
            print("公司节点: " + line_b + "***时间戳：" + line_c + "***图片路径：" + line_d+"***节点简称："+line_e+"\n")
            file_in.write("公司节点:***" + line_b + "***" + line_c + "***" + line_d + "***"+line_e+"***\n")
        else:
            if line_b.endswith('百度一下') or "百度一下" in line_b or "搜一下" in line_b:
                if len(line_b) > 9:
                    line_e = line_b[0:9] + "..."
                else:
                    line_e = line_b
                print("百度搜索框: " + line_b + " 时间戳:" + line_c + " 图片路径:" + line_d + "***节点简称："+line_e+"\n")
                file_in.write("百度搜索框:***" + line_b + "***" + line_c + "***" + line_d + "***"+line_e+"***\n")
            else:
                if line_b.endswith('搜索') or line_b.endswith('搜索一下') or '搜索'in line_b or '搜索一下'in line_b:
                    if len(line_b) > 9:
                        line_e = line_b[0:9]+"..."
                    else:
                        line_e = line_b
                    line_last = line_b
                    print("输入框节点:***" + line_b + " 时间戳：" + line_c + " 图片路径：" + line_d+"***节点简称："+line_e+"\n")
                    file_in.write("输入框节点:***" + line_b + "***" + line_c + "***" + line_d + "***"+line_e+"***\n")
                else:
                    if "输入企业法定代表人" in line_last:
                        if len(line_b) > 9:
                            line_e = line_b[0:9] + "..."
                        else:
                            line_e = line_b
                        print("法人节点：" + line_b + " 时间戳：" + line_c + " 图片路径：" + line_d+"***节点简称："+line_e+"\n")
                        file_in.write("法人节点:***" + line_b + "***" + line_c + "***" + line_d + "***"+line_e+"***\n")
                    else:
                        if len(line_b) > 9:
                            line_e = line_b[0:9] + "..."
                        else:
                            line_e = line_b
                        print("用户点击：" + line_b + " 时间戳：" + line_c + " 图片路径：" + line_d+"***节点简称："+line_e+"\n")
                        file_in.write("用户点击:***" + line_b + "***" + line_c + "***" + line_d + "***"+line_e+"***\n")
def textOCR(file_img, text_url, file_result, file_move):
        cont = -1
        cont2 = 0
        str5 = ''
        print(sys._getframe().f_code.co_name)  # 当前函数名
        print(sys._getframe().f_lineno)  # 当前行号
        filename_in = file_img
        for parent, dirnames, filenames in os.walk(filename_in):
            for filename in filenames:
                file_handle = open(text_url, 'a+')
                filename_out = file_result
                # filename = os.path.join(parent,filename)
                time = []
                x, y, time = filenamesplit(filename)
                file_in = filename_in + filename
                file_out = filename_out + filename
                im3 = zonghe(os.path.join(filename_in, filename), y, x, os.path.join(file_result, filename),
                             os.path.join(
                                 file_move, filename))
                # print("step  one is ok")
                # print("step  two is ok")
                str1 = []
                str1 = OCR(os.path.join(file_result, filename))
                # 时间不显示年份
                # str2 = time[0] + "/" + time[1] + "/" + time[2] + " " + time[3] + ":" + time[4] + ":" + time[5]
                str2 = time[1] + "/" + time[2] + " " + time[3] + ":" + time[4] + ":" + time[5]
                str4 = ''
                for i in range(len(str1)):
                    str4 = str4 + str1[i] + ' '
                str4 = str4.replace('***', '')
                print(str4+"@@@@\n")
                if node_name_filter(str4):
                    continue
                if len(str4) != 0 and '公司' in str4:

                    if (str4 == str5) == False or (str5.split('公')[0] == str4.split('公')[0]) == False:
                        cont = 1
                        file_handle.write(
                            str(cont) + "***" + str4 + "***" + str2 + "***" + filename_in + filename + "***" + "\n")

                if len(str4) != 0 and '公司' not in str4 and '搜索' not in str4:

                    if str4 != str5:
                        cont = cont + 1
                        file_handle.write(
                            str(cont) + "***" + str4 + "***" + str2 + "***" + filename_in + filename + "***" + "\n")
                if len(str4) != 0 and '公司' not in str4 and '搜索' in str4:

                    if str4 != str5:
                        cont = 0
                        file_handle.write(
                            str(cont) + "***" + str4 + "***" + str2 + "***" + filename_in + filename + "***" + "\n")
                file_handle.close()
                str5 = str4
                import time
                time.sleep(0.5)
                print("end")

if __name__ == '__main__':
    # cont = -1
    # cont2 = 0
    # str5 = ''
    # def textOCR(file_img, text_url, file_result, file_move):
    #     print(sys._getframe().f_code.co_name)  # 当前函数名
    #     print(sys._getframe().f_lineno)  # 当前行号
    #     filename_in = file_img
    #     global cont
    #     global cont2
    #     global str5
    #     for parent, dirnames, filenames in os.walk(filename_in):
    #         for filename in filenames:
    #             file_handle = open(text_url, 'a+')
    #             filename_out = file_result
    #             # filename = os.path.join(parent,filename)
    #             time = []
    #             x, y, time = filenamesplit(filename)
    #             file_in = filename_in + filename
    #             file_out = filename_out + filename
    #             im3 = zonghe(os.path.join(filename_in, filename), y, x, os.path.join(file_result, filename),
    #                          os.path.join(
    #                              file_move, filename))
    #             # print("step  one is ok")
    #             # print("step  two is ok")
    #             str1 = []
    #             str1 = OCR(os.path.join(file_result, filename))
    #             # 时间不显示年份
    #             # str2 = time[0] + "/" + time[1] + "/" + time[2] + " " + time[3] + ":" + time[4] + ":" + time[5]
    #             str2 = time[1] + "/" + time[2] + " " + time[3] + ":" + time[4] + ":" + time[5]
    #             str4 = ''
    #             for i in range(len(str1)):
    #                 str4 = str4 + str1[i] + ' '
    #             str4 = str4.replace('***', '')
    #             print(str4+"@@@@\n")
    #             if node_name_filter(str4):
    #                 continue
    #             if len(str4) != 0 and '公司' in str4:
    #
    #                 if (str4 == str5) == False or (str5.split('公')[0] == str4.split('公')[0]) == False:
    #                     cont = 1
    #                     file_handle.write(
    #                         str(cont) + "***" + str4 + "***" + str2 + "***" + filename_in + filename + "***" + "\n")
    #
    #             if len(str4) != 0 and '公司' not in str4 and '搜索' not in str4:
    #
    #                 if str4 != str5:
    #                     cont = cont + 1
    #                     file_handle.write(
    #                         str(cont) + "***" + str4 + "***" + str2 + "***" + filename_in + filename + "***" + "\n")
    #             if len(str4) != 0 and '公司' not in str4 and '搜索' in str4:
    #
    #                 if str4 != str5:
    #                     cont = 0
    #                     file_handle.write(
    #                         str(cont) + "***" + str4 + "***" + str2 + "***" + filename_in + filename + "***" + "\n")
    #             file_handle.close()
    #             str5 = str4
    #             import time
    #             time.sleep(0.5)
    #             print("end")
    file_img = '../vue/public/image/172.17.173.51/'
    file_move = '../vue/public/image_move/172.17.173.51/'
    file_result = '../vue/public/result/'
    password = '123456'
    from data_deal.neo4j import *
    from data_deal.clearText import *

    db = Graph("http://localhost:7474/", username="neo4j", password=password)
    first = Node('UserClick', name='开始', time='', address='', pieaddress='', nodeJname='开始')
    node = []
    edge = []
    last = '*'
    db.create(first)
    lastS = Node()
    a = Node()
    b = first
    c = Node()
    d = Node()
    while( True ):
        textOCR(file_img, text_in, file_result, file_move)
        time.sleep(1)
        file = open(text_in, 'r')
        file_in = open(text_out, 'w')
        lines = file.readlines()
        line_lastcom = "*"
        line_last = '*'
        for line in lines:
            print(lines)
            lineStr = line.split('***')
            line_a = lineStr[0]
            line_b = lineStr[1].rstrip()
            # line_b = node_name_filter(line_b)
            print(line_b)
            line_c = lineStr[2].strip()
            line_d = 'image/pic' + lineStr[3].strip().split('pic')[1]
            if (line_b.endswith('公司') or line_b.endswith('酒店') or line_b.endswith('工厂')) and (
                    line_lastcom not in line_b and line_lastcom != line_b):
                line_lastcom = line_b
                if len(line_b) > 9:
                    line_e = line_b[0:9] + "..."
                else:
                    line_e = line_b
                print("公司节点: " + line_b + "***时间戳：" + line_c + "***图片路径：" + line_d + "***节点简称：" + line_e + "\n")
                file_in.write("公司节点:***" + line_b + "***" + line_c + "***" + line_d + "***" + line_e + "***\n")
            else:
                if line_b.endswith('百度一下') or "百度一下" in line_b or "搜一下" in line_b:
                    if len(line_b) > 9:
                        line_e = line_b[0:9] + "..."
                    else:
                        line_e = line_b
                    print("百度搜索框: " + line_b + " 时间戳:" + line_c + " 图片路径:" + line_d + "***节点简称：" + line_e + "\n")
                    file_in.write("百度搜索框:***" + line_b + "***" + line_c + "***" + line_d + "***" + line_e + "***\n")
                else:
                    if line_b.endswith('搜索') or line_b.endswith('搜索一下') or '搜索' in line_b or '搜索一下' in line_b:
                        if len(line_b) > 9:
                            line_e = line_b[0:9] + "..."
                        else:
                            line_e = line_b
                        line_last = line_b
                        print("输入框节点:***" + line_b + " 时间戳：" + line_c + " 图片路径：" + line_d + "***节点简称：" + line_e + "\n")
                        file_in.write("输入框节点:***" + line_b + "***" + line_c + "***" + line_d + "***" + line_e + "***\n")
                    else:
                        if "输入企业法定代表人" in line_last:
                            if len(line_b) > 9:
                                line_e = line_b[0:9] + "..."
                            else:
                                line_e = line_b
                            print("法人节点：" + line_b + " 时间戳：" + line_c + " 图片路径：" + line_d + "***节点简称：" + line_e + "\n")
                            file_in.write(
                                "法人节点:***" + line_b + "***" + line_c + "***" + line_d + "***" + line_e + "***\n")
                        else:
                            if len(line_b) > 9:
                                line_e = line_b[0:9] + "..."
                            else:
                                line_e = line_b
                            print("用户点击：" + line_b + " 时间戳：" + line_c + " 图片路径：" + line_d + "***节点简称：" + line_e + "\n")
                            file_in.write(
                                "用户点击:***" + line_b + "***" + line_c + "***" + line_d + "***" + line_e + "***\n")
        file_handle = open(text_out, 'r')
        lines = file_handle.readlines()
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
                lastS = Node('SelectNode', name=nodeName, time=nodeTime, address=nodeAddress, pieaddress='',
                             nodeJname=nodeJname)
                db.create(lastS)
            if nodeId == '用户点击:':
                a = Node('UserClick', name=nodeName, time=nodeTime, address=nodeAddress, pieaddress='',
                         nodeJname=nodeJname)
                db.create(a)
            if nodeId == '公司节点:':
                a = Node('CompanyNode', name=nodeName, time=nodeTime, address=nodeAddress, pieaddress='',
                         nodeJname=nodeJname)
                db.create(a)
            if nodeId == '百度搜索框:':
                a = Node('BaiduNode', name=nodeName, time=nodeTime, address=nodeAddress, pieaddress='',
                         nodeJname=nodeJname)
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
        time.sleep(1)
        # clearText(text_in)
        # clearText(text_out)


