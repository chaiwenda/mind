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
import time
# from py2neo import Graph, Node, Relationship
import sys
from py2neo import Graph, Node, Relationship
import  shutil


# 文件名分割
def filenamesplit(filename):
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
    cv2.imwrite(filename, im_in)


def zonghe(filename_in, mouse_x, mouse_y, filename_out, move_in, file_out2):
    print("move_in" + move_in)
    print("filename_in" + filename_in)
    print("filename_out" + filename_out)
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
        if isb == 1 and area > 10 and area < 50000 and zhoucb < 1.3 and zhoucb > 0.9 and kgb > 1.8 and kgb < 50:  # if isb[i] == 1 and area > 100 and zhoucb >0.8 and zhoucb<2 and kgb >=2 and kgb < 30:#if isb[i] == 1 and area > 10 and zhoucb < 1.3 and zhoucb > 0.9 and kgb > 5 and kgb < 30:  #if   isb[i]==1 :#if isb[i] == 1 and zhoucb < 1.3 and zhoucb > 0.9 and kgb > 5 and kgb < 30:#if isb[i] == 1 and area < (im1.shape[0] * im1.shape[1])/3:#if isb[i] == 1 and area > 10000 and zhoucb < 1.3 and zhoucb > 0.9 and kgb > 5 and kgb < 30:#if   isb[i]==1 :
            # cv2.drawContours(im3, contours, i, 255, 1)
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
            cv2.imwrite(file_out2, im_out)
            return im3
        else:
            pass
    im3 = ones((20,20))
    save_img(filename_out, im3)
    cv2.rectangle(im_out, (0 , 0), (20, 20), 255, 2)
    im_out[mouse_x:mouse_x + 10, mouse_y:mouse_y + 10, 0] = 0
    im_out[mouse_x:mouse_x + 10, mouse_y:mouse_y + 10, 1] = 255
    im_out[mouse_x:mouse_x + 10, mouse_y:mouse_y + 10, 2] = 0
    cv2.imwrite(file_out2, im_out)
    time.sleep(1)
    return im3

# 节点过滤系统
def node_name_filter(node_name, file_filter_path):
    filter_lists = []
    with open(file_filter_path, 'r') as f:
        for line_msg in f:
            filter_lists.append(line_msg.strip('\n').strip(' '))
    for filter_list in filter_lists:
            if filter_list.strip(" ") == node_name.strip(" "):
                f.close()
                return True
    f.close()
    return False

# 节点过滤整合系统
def node_name_filter2(node_name, file_filter_path):
    filter_lists = []
    with open(file_filter_path, 'r') as f:
        for line_msg in f:
            filter_lists.append(line_msg.strip('\n').strip(' '))
    for filter_list in filter_lists:
            if node_name.strip("\n").strip(' ').endswith(filter_list.strip("\n").strip(" ")) == True:
                f.close()
                return filter_list.strip("\n").strip(" ")
    f.close()
    return "false"

# 节点信息处理系统
def txt_name_filter(read_file_path , filter_file_path):
    print("==========txt1 文本信息处理系统============")
    print("read_file_path = " + read_file_path)
    print("filter_file_path = " + filter_file_path)
    message_lists = []
    filter_lists = []
    with open(filter_file_path, 'r') as f:
        for line_msg in f:
            filter_lists.append(line_msg.strip('\n').strip(' '))
    f.close()
    with open(read_file_path, 'r') as f1:
        for line_msg1 in f1:
            line_msg2 = line_msg1.split('***')[1].split("***")[0].strip(' ').strip('\n')
            print("当前处理的词条是:%s"%(line_msg2))
            for item in filter_lists:
                if item in line_msg2:
                    print("%s出现了"%(item))
                    strNone = ''
                    line_msg2 = line_msg2.replace(item, strNone).strip('\n').strip(' ')
            if line_msg2 != '':
                replace_source = line_msg1.split('***')[1].split("***")[0]
                print("需要替换的节点是：%s" % (replace_source))
                print("替换后的节点是：%s" % (line_msg2))
                line_msg1 = line_msg1.replace(replace_source,line_msg2)
            print("处理后的词条是=%s\n"%(line_msg1))
            message_lists.append(line_msg1)
    f1.close()
    print("==========txt1 文本信息处理系统 end============")
    return message_lists
def OCR(filename):
    #'10792304', 'R2xOMHZhykHekhucL526RctZ', 'ldfAKMLBPXkqgGrQQwjBeK1hF56CwB4C'
    # 'nio = ['10792304', 'R2xOMHZhykHekhucL526RctZ', 'ldfAKMLBPXkqgGrQQwjBeK1hF56CwB4C']
    # x_w = ['10798308', 'nKpoZturaOHjlYGQS9q8HAmU', 'nSGzmGkS7jZ1vGxuiraYEki2ACKtVEXs']
    # w_d = ['10798308', 'jfPrTkedpNDurbAtkuS7N6D6', '4mGMQrLqNzznKpRPltaw9WqFWCuEOxaG']
    # y_f = ['10816490', 'KMe18P0lSkaVjp6j4eWKqFp7', 'BP01DVaH4NTP2W2LRPireKRvuEidlOh3']'
    # APP_ID = '11418443'
    # API_KEY = 'od6MXy9DvM3TTvHVpIsalgSO'
    # SECRET_KEY = '1eoLKrIvpts8oKOysNfDvtK9nVffxCnD'
    API_ID = ['10792304','10798308','10816490','11418443']
    API_KEY = ['R2xOMHZhykHekhucL526RctZ', 'nKpoZturaOHjlYGQS9q8HAmU','KMe18P0lSkaVjp6j4eWKqFp7','od6MXy9DvM3TTvHVpIsalgSO']
    SECRET_KEY = ['ldfAKMLBPXkqgGrQQwjBeK1hF56CwB4C', 'nSGzmGkS7jZ1vGxuiraYEki2ACKtVEXs', 'BP01DVaH4NTP2W2LRPireKRvuEidlOh3','1eoLKrIvpts8oKOysNfDvtK9nVffxCnD']
    OCR_handle = open("../Filter/OCR_times.txt","r")
    number = OCR_handle.readline()
    OCR_handle.close()
    if number != '':
        number = int(number)
    else:
        print("txt内容为空")
    if number >= 0 and number <= 499:
        client = AipOcr(API_ID[0], API_KEY[0], SECRET_KEY[0])
        number = number + 1
        OCR_handle = open("../Filter/OCR_times.txt", "w")
        OCR_handle.write(str(number))
        OCR_handle.close()
    elif number >499 and number <= 999:
        client = AipOcr(API_ID[1], API_KEY[1], SECRET_KEY[1])
        number = number + 1
        OCR_handle = open("../Filter/OCR_times.txt", "w")
        OCR_handle.write(str(number))
        OCR_handle.close()
    elif number >999 and number <= 1499:
        client = AipOcr(API_ID[1], API_KEY[1], SECRET_KEY[1])
        number = number + 1
        OCR_handle = open("../Filter/OCR_times.txt", "w")
        OCR_handle.write(str(number))
        OCR_handle.close()
    elif number >1499 and number <= 1999:
        client = AipOcr(API_ID[1], API_KEY[1], SECRET_KEY[1])
        number = number + 1
        OCR_handle = open("../Filter/OCR_times.txt", "w")
        OCR_handle.write(str(number))
        OCR_handle.close()
    else:
        print("OCR次数到限，请更换账号")
        return ''
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
    # print(result)
    for i in range(len(result['words_result'])):
        string.append(result["words_result"][i]["words"])
    return string

# 信息写入系统
def writen_txt(read_file_path, writer_file_path, filter_file_path):
    print("msg_lists")
    with open(writer_file_path, 'w') as f:
        msg_lists = txt_name_filter(read_file_path , filter_file_path)
        print("msg_lists")
        print(msg_lists)
        msg = ''
        for item in msg_lists:
            msg = msg + str(item)
        if msg != "":
            print("text内容不为空" + msg)
        f.write(msg)
    f.close()
# 判断是否是公司
def companyDetect(word_name):
    end_name_lists = []
    end_name_path = '../Filter/endName.txt'
    with open(end_name_path, 'r') as f:
        for line_msg in f:
            if word_name.strip('\n').strip(' ').endswith(line_msg.strip('\n').strip(' ')):
                print("%s是公司节点"%(word_name))
                return True
        return False
# 判断是否是百度搜索节点
def baiduDetect(word_name):
    end_name_lists = []
    endname = ""
    end_name_path = '../Filter/baidu.txt'
    with open(end_name_path, 'r') as f:
        endname = "False"
        for line_msg in f:
            if word_name.strip('\n').strip(' ').endswith(line_msg.strip('\n').strip(' ')):
                print("%s是百度节点"%(word_name))
                endname = word_name
                break
    return endname

# 判断是否是搜索节点
def searchDetect(word_name):
    end_name_lists = []
    end_name_path = '../Filter/search.txt'
    with open(end_name_path, 'r') as f:
        for line_msg in f:
            if word_name.strip('\n').strip(' ').endswith(line_msg.strip('\n').strip(' ')):
                print("%s是搜索节点"%(word_name))
                return True
        return False
def write_define_word(read_file_path, writer_file_path):
    print("================write_define_word start=================")
    file_handle = open(writer_file_path, 'w')
    message = []
    MSG = ''
    with open(read_file_path, 'r') as f:
        for line_msg1 in f:
            lineStr = line_msg1.split('***')
            line_b = lineStr[1].strip('')  # 节点名称
            line_c = lineStr[2].strip('')  # 时间
            line_d = lineStr[3].strip('')  # 地址
            nodeJname = ''
            xxx = "***"
            if len(line_b) > 9:
                nodeJname = line_b[0:9] + "..."
            if len(line_b) != 0 and searchDetect(line_b) == True:  # 搜索
                    filter_file_path = '../Filter/search.txt'
                    replaceName = node_name_filter2(line_b, filter_file_path)
                    print("replaceName" + replaceName)
                    line_b ="搜索：" + line_b.replace(replaceName, '').strip(' ')
                    cont = 0
                    msg = str(cont) + xxx + line_b + xxx + line_c + xxx + line_d + xxx + nodeJname
                    message.append(msg)
            elif len(line_b) != 0 and companyDetect(line_b) == True:  # 公司
                    line_b = "公司节点：" + line_b.strip(' ')
                    cont = 1
                    msg = str(cont) + xxx + line_b + xxx + line_c + xxx + line_d + xxx + nodeJname
                    message.append(msg)
            elif len(line_b) != 0 and baiduDetect(line_b) != 'False':  # 百度搜索
                filter_file_path = '../Filter/baidu.txt'
                replaceName = node_name_filter2(line_b, filter_file_path)
                print("replaceName" + replaceName)
                line_b = "百度搜索：" + line_b.replace(replaceName, '').strip(' ')
                cont = 2
                msg = str(cont) + xxx + line_b + xxx + line_c + xxx + line_d + xxx + nodeJname
                message.append(msg)
            elif len(line_b) != 0 and baiduDetect(line_b) == "False":  # 自由搜索
                cont = 2
                msg = str(cont) + xxx + line_b + xxx + line_c + xxx + line_d + xxx + nodeJname
                message.append(msg)
            else:
                x = 1
        for item in message:
            MSG = MSG + item + '\n'
        file_handle.write(MSG)
    file_handle.close()
    f.close()
    print("================write_define_word end=================")
def filter4_file(writer_file_path2, writer_file_path4):
    # 原则一：首行是否为0
    print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
    # clearText(writer_file_path4)
    file = open(writer_file_path2, 'r')
    lines = file.readlines()
    print(lines)
    Msg = ''
    if len(lines) == 0:
        print("文件四文本为空")
        return 0
    if lines[0].split("***")[0].strip(" ") != '0':
        print("第一行不是0")
        lines[0] = "0***搜索：noName***noTime***noAddress***nodeJname\n" + lines[0]
    Msg = Msg + lines[0]
    for line in lines[1:]:
        Msg = Msg + line
    print("{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}")
    print(Msg)
    print("{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}")
    with open(writer_file_path4, 'w') as f:
        f.write(Msg)
    f.close()
    # 原则2：0 2之间是否有1
    file = open(writer_file_path4, 'r')
    lines2 = file.readlines()
    print(lines2)
    print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
    Msg = ''
    if len(lines2) == 0:
        print("文本3为空")
        return 0
    Msg = Msg + lines2[0]
    for line2 in lines2[1:]:
        index_line = lines2.index(line2)
        if line2.split("***")[0] == '2':
            if lines2[index_line - 1].split("***")[0].strip(" ") == '0':
                line2 = "1***noName***noTime***noAddress***noNodeJname\n" + line2
                print("添加信息：" + "1***noName***noTime***noAddress\n")
        Msg = Msg + line2
    print("MSG===================\n"+Msg)
    # Msg.replace("\\","/").replace("\\\\","/")
    with open(writer_file_path4, 'w') as f:
        f.write(Msg)
        f.close()


def textOCR(file_img, text_url, file_result, file_move):
    file_filter_path = '../Filter/filter_file3.txt'
    cont = -1
    filename_in = file_img
    filenames = os.listdir(file_img)
    print("filenames = %s"%(filenames))
    if len(filenames) == 0:
        return 0
    for filename in filenames:
        try:
            file_handle = open(text_url, 'a+')
            filename_out = file_result
            time = []
            x, y, time = filenamesplit(filename)
            file_in = filename_in + filename
            # file_out = os.path.join(file_move, filename)
            file_times_handle = open("../Filter/Round_iteration_number.txt")
            number = file_times_handle.readline()
            file_out1 = os.path.join(file_move, str(number))
            file_out2 = os.path.join(file_out1, filename)
            if not os.path.exists(file_out1):
                os.makedirs(file_out1)
            im3 = zonghe(os.path.join(filename_in, filename), y, x, os.path.join(file_result, filename), file_out1, file_out2)
            str1 = []
            str1 = OCR(os.path.join(file_result, filename))
            # 时间不显示年份
            str2 = time[1] + "/" + time[2].strip(' ').strip('\n') + " " + time[3] + ":" + time[4] + ":" + time[5]
            str4 = ''
            for i in range(len(str1)):
                str4 = str4 + str1[i] + ' '
            str4 = str4.replace('***', '')
            if node_name_filter(str4, file_filter_path):
                print(str4 + "被过滤掉了")
                continue
            if str4 != '':
                try:
                    message_write = "***" + str4 + "***" + str2.strip(' ').strip(
                        '\n') + "***" + filename_in + filename + "***" + "\n"
                    message_write.replace("\\", "/")
                    message_write.replace("\\\\", "/")
                    file_handle.write(message_write)
                except UnicodeEncodeError:
                    print("UnicodeEncodeError +  message_write\n + " + message_write)
            file_handle.close()
            import time
            time.sleep(0.5)
            print("***" + str4 + "***" + str2 + "***" + filename_in + filename + "***" + "\n")
            print("end")
        except FileNotFoundError:
            continue
    return 1

def clearText(texturl):
    file = open(texturl,'r+')
    file.truncate()

if __name__ == '__main__':
    filter_file_path = '../Filter/filter_file.txt'
    file_path = '../nodeName/result1.txt'
    file_img = 'F:/cwd/mind_test/django_test2/vue/public/image/172.17.173.51/'
    file_move = 'F:/cwd/mind_test/django_test2/vue/public/image_move/172.17.173.51/'
    file_result = 'F:/cwd/mind_test/django_test2/vue/public/result/'
    read_file_path = '../nodeName/result1.txt'
    writer_file_path = '../nodeName/result2.txt'
    writer_file_path2 = '../nodeName/result3.txt'
    writer_file_path4 = '../nodeName/result4.txt'
    address = "http://localhost:7474/"
    password = '123456'

    db = Graph(address, username="neo4j", password=password)
    first = Node('UserClick', name='开始', time='', address='', pieaddress='', nodeJname='开始')
    db.create(first)
    # b = first
    lastS = Node()
    a = first
    b = first
    c = first
    d = first

    def neo4jwrite(writer_file_path2, writer_file_path4, address, password):
        print("==============neo4jwrite start===================")
        file_handle = open(writer_file_path4, 'r')
        lines = file_handle.readlines()
        node = []
        edge = []
        last = '*'
        db = Graph(address, username="neo4j", password=password)
        global first

        # first = Node('UserClick', name='开始', time='', address='', pieaddress='', nodeJname='开始')
        # db.create(first)
        global lastS
        global a
        global b
        global c
        global d
        for line in lines:
            print(line, type(line))
            result = line.split("***")
            print(result, len(result))
            nodeId = result[0].strip(' ')
            nodeName = result[1]
            nodeTime = result[2]
            nodeAddress = result[3].strip()
            nodeJname = result[4]
            print('*' + nodeId + '*')
            if nodeId == '0':
                # lastS = Node('SelectNode', name=nodeName, time=nodeTime, address=nodeAddress, pieaddress='', nodeJname=nodeJname)
                lastS = Node('SelectNode', name=nodeName, time=nodeTime, address=nodeAddress, pieaddress='',
                             nodeJname=nodeJname)
                db.create(lastS)
            if nodeId == '2':
                a = Node('UserClick', name=nodeName, time=nodeTime, address=nodeAddress, pieaddress='',
                         nodeJname=nodeJname)
                db.create(a)
            if nodeId == '1':
                a = Node('CompanyNode', name=nodeName, time=nodeTime, address=nodeAddress, pieaddress='',
                         nodeJname=nodeJname)
                db.create(a)
            if nodeId == '0':
                relation = Relationship(first, 'Click', lastS)
                db.create(relation)
            if nodeId == '2':
                relation = Relationship(b, 'ClickList', a)
                db.create(relation)
            if nodeId == '1':
                relation = Relationship(lastS, 'ClickCompany', a)
                db.create(relation)
            b = a
            last = nodeId
            # clearText("..\\nodeName\\result4.txt")
        print("==============neo4jwrite end===================")
    i = 0
    j = 0
    sum_time_no_solving = 0
    sleep_time = 5
    while True:
        import time
        time.sleep(sleep_time)
        image_file_lists = []
        return_number = textOCR(file_img, read_file_path, file_result, file_move)
        # 如果图片太少则不做处理
        if return_number == 0:
            print("无图片传入")
            sum_time_no_solving = sum_time_no_solving + 1
            if sum_time_no_solving == 20:
                sleep_time = 10
            if sum_time_no_solving == 40:
                sleep_time = 20
            continue
        #     filter_file_path = '../Filter/filter_file.txt'
        #     file_path = '../nodeName/result1.txt'
        #     file_img = 'F:\\cwd\\mind_test\\django_test2\\vue\public\\image\\172.17.173.51\\'
        #     file_move = 'F:\\cwd\\mind_test\\django_test2\\vue\public\\image_move\\172.17.173.51\\'
        #     file_result = 'F:\\cwd\\mind_test\\django_test2\\vue\public\\result\\'
        #     read_file_path = '../nodeName/result1.txt'
        #     writer_file_path = '../nodeName/result2.txt'
        #     writer_file_path2 = '../nodeName/result3.txt'
        #     writer_file_path4 = '../nodeName/result4.txt'
        #     address = "http://localhost:7474/"
        #     password = '123456'
        def open_txt(file_path):
            h = open(file_path)
            x = h.readlines()
            return len(x)
        writen_txt(read_file_path, writer_file_path, filter_file_path)  #txt1->txt2
        if open_txt("../nodeName/result1.txt") >= 1:
            shutil.copyfile("../nodeName/result1.txt", "../nodeName_remove/result1/result1_log" + str(i) + ".txt")
            clearText("../nodeName/result1.txt")
        write_define_word(writer_file_path, writer_file_path2)     # txt2->txt3
        if open_txt("../nodeName/result2.txt") >= 1:
            shutil.copyfile("../nodeName/result2.txt", "../nodeName_remove/result2/result2_log" + str(i) + ".txt")
            clearText("../nodeName/result2.txt")
        else:
            print("文件2为空")
        filter4_file(writer_file_path2, writer_file_path4)    # txt3->txt4
        if open_txt("../nodeName/result3.txt") >= 1:
            shutil.copyfile("../nodeName/result3.txt", "../nodeName_remove/result3/result3_log" + str(i) + ".txt")
            clearText("../nodeName/result3.txt")
        else:
            print("文件3为空")
        neo4jwrite(writer_file_path2, writer_file_path4, address, password)
        if open_txt("../nodeName/result4.txt") >= 1:
            shutil.copyfile("../nodeName/result4.txt", "../nodeName_remove/result4/result4_log" + str(i) + ".txt")
            clearText("../nodeName/result4.txt")
        else:
            print("文件4为空")
        i = i + 1
        sleep_time = 5
        handle_Round_iteration_number = open("../Filter/Round_iteration_number.txt", "r")
        number = handle_Round_iteration_number.readline()
        j = i
        if j % 3 == 0:
            number = int(number) + 1
        handle_Round_iteration_number.close()
        handle_Round_iteration_number = open("../Filter/Round_iteration_number.txt", "w")
        handle_Round_iteration_number.write(str(number))
        handle_Round_iteration_number.close()
        # break