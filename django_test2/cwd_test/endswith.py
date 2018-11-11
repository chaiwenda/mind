# coding:utf-8

# xxx_lists = ["公司","磨坊"]
# strint_name = "sdfsfsfaaa磨坊"
# for item in xxx_lists:
#     if strint_name.endswith(item):
#         print("yes")
def open_txt(file_path):
    h = open(file_path)
    x = h.readlines()
    return len(x)
xxx = open_txt("../nodeName/result1.txt")
print(xxx)