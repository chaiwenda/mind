# encoding: utf-8
"""
对返回的text文档进行进一步处理，识别出公司节点、输入框节点、百度搜索框节点、用户点击节点
"""
def textDeal(text_in,text_out):
    file = open(text_out, 'r')
    file_in = open(text_in, 'w+')
    lines = file.readlines()
    line_lastcom = "*"
    line_last = '*'
    for line in lines:
        print(lines)
        lineStr = line.split('***')
        line_a = lineStr[0].strip('')  # 属性
        line_b = lineStr[1].strip('')  # 节点名称
        line_b = lineStr[2].strip('')  # 时间
        line_b = lineStr[3].strip('')  # 地址
        line_b = node_name_filter(line_b)
        print(line_b)
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


def node_name_filter(node_name):
    # 过滤文件内容存在txt文件里
    file_filter_path = '../Filter/filter_file.txt'
    filter_lists = []
    with open(file_filter_path, 'r') as f:
        for line_msg in f:
            # print(line_msg.strip('\n'))
            filter_lists.append(line_msg.strip('\n').strip(' '))
    # filter_lists = ["企业名称", "信用编码", "法定代表人", "股东", "失信被执行人", "查企业信用，到11315.cm", '选择地区','百度一下你就知道','请输入企业名称']
    for filter_list in filter_lists:
            if filter_list in node_name:
                print(node_name.split(filter_list))
                name_lists = node_name.split(filter_list)
                node_name = ''
                for item in name_lists:
                    node_name += item
    return node_name


if __name__ == '__main__':
    textDeal('e:/django_project/vue\public/result2.txt', 'e:/django_project/vue/public/result1.txt')







