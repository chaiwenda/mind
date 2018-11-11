import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")# project_name 项目名称
django.setup()
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
def get_json(request,str_name):
        list_out = []
        from data_deal.children import children3
        from data_deal.json1 import makeJson
        import json
        list1 = children3(str_name, '123456')
        if len(list1) == 0:
            return HttpResponse("none data get")
        else:
            #list_out["node_list"] = list1
            for i in range(len(list1)):
                list_out.append(json.loads(makeJson(list1[i]['name'], list1[i]['time'], '', '')))
            #str1 = '{"node_list": [{"name": "\u5f00\u59cb", "time": ""}], "name0": {"Graph": {"tree": {"name": "\u5f00\u59cb", "proof": "123456", "time": "", "children": [{"name": "\u4f01\u4e1a\u540d\u79f0\u4fe1\u7528\u7f16\u7801\u6cd5\u5b9a\u4ee3\u8868\u4eba\u80a1\u4e1c\u5931\u4fe1\u88ab\u6267\u884c\u4eba \u5c0f\u7c73 \u9009\u62e9\u5730\u533a\u641c\u7d22", "proof": "F:/untitled2/img/pic_2018_09_20_21_53_12(1404225)[mouse1].jpg", "time": "2018/09/20 21:53:12", "children": [{"name": "\u90a2\u53f0\u53bf\u90c1\u79cb\u5c0f\u7c73\u52a0\u5de5\u5382\u4fe1\u7528\u53ef\u67e5\u8be2\u7f51\u7ad9 \u90a2\u53f0\u53bf\u90c1\u79cb\u5c0f\u7c73\u52a0\u5de5\u5382", "proof": "F:/untitled2/img/pic_2018_09_20_21_53_25(662560)[mouse0].jpg", "time": "2018/09/20 21:53:25", "children": [{"name": "2153 s+2018/9/20", "proof": "F:/untitled2/img/pic_2018_09_20_21_53_42(6531063)[mouse0].jpg", "time": "2018/09/20 21:53:42", "children": []}, {"name": "\u957f\u5bff\u8944", "proof": "F:/untitled2/img/pic_2018_09_20_21_53_40(619664)[mouse0].jpg", "time": "2018/09/20 21:53:40", "children": []}, {"name": "\u5f20\u6d77\u666e", "proof": "F:/untitled2/img/pic_2018_09_20_21_53_38(616600)[mouse0].jpg", "time": "2018/09/20 21:53:38", "children": []}, {"name": "\u5a01\u53bf\u6052\u4f73\u5c0f\u7c73\u52a0\u5de5\u5382\u4fe1\u7528\u53ef\u67e5\u8be2\u7f51\u7ad9", "proof": "F:/untitled2/img/pic_2018_09_20_21_53_37(631556)[mouse0].jpg", "time": "2018/09/20 21:53:37", "children": []}, {"name": "\u5a01\u53bf\u6052\u4f73\u5c0f\u7c73\u52a0\u5de5", "proof": "F:/untitled2/img/pic_2018_09_20_21_53_35(567502)[mouse0].jpg", "time": "2018/09/20 21:53:35", "children": []}, {"name": "\u4fe1\u90a2\u53f0\u53bf\u90c1\u79cb\u5c0f\u7c73\u52a0\u5de5\u5382\u4fe1\u7528\u6863", "proof": "F:/untitled2/img/pic_2018_09_20_21_53_32(1562103)[mouse0].jpg", "time": "2018/09/20 21:53:32", "children": []}, {"name": "\u90a2\u53f0\u53bf\u4f1a\u5b81\u9547\u65f6\u6751", "proof": "F:/untitled2/img/pic_2018_09_20_21_53_28(650726)[mouse0].jpg", "time": "2018/09/20 21:53:28", "children": []}, {"name": "\u6cb3\u5317\u7701\u90a2\u53f0\u5e02\u90a2\u53f0\u53bf\u4f1a\u5b81\u9547\u65f6\u6751", "proof": "F:/untitled2/img/pic_2018_09_20_21_53_26(657694)[mouse0].jpg", "time": "2018/09/20 21:53:26", "children": []}]}]}, {"name": "\u4f01\u4e1a\u540d\u79f0\u4fe1\u7528\u7f16\u7801\u6cd5\u5b9a\u4ee3\u8868\u4eba\u80a1\u4e1c\u5931\u4fe1\u88ab\u6267\u884c\u4eba \u8bf7\u8f93\u5165\u4f01\u4e1a\u540d\u79f0 \u9009\u62e9\u5730\u533a\u641c\u7d22", "proof": "F:/untitled2/img/pic_2018_09_20_21_53_08(1074225)[mouse0].jpg", "time": "2018/09/20 21:53:08", "children": []}, {"name": "\u4f01\u4e1a\u540d\u79f0\u4fe1\u7528\u7f16\u7801\u6cd5\u5b9a\u4ee3\u8868\u4eba\u80a1\u4e1c\u5931\u4fe1\u88ab\u6267\u884c\u4eba \u534e\u4e3a \u9009\u62e9\u5730\u533a\u641c\u7d22", "proof": "F:/untitled2/img/pic_2018_09_20_21_52_27(1038225)[mouse0].jpg", "time": "2018/09/20 21:52:27", "children": [{"name": "\u534e\u4e3a\u6280\u672f\u6709\u9650\u516c\u53f8", "proof": "F:/untitled2/img/pic_2018_09_20_21_52_46(516646)[mouse0].jpg", "time": "2018/09/20 21:52:46", "children": [{"name": "\u738b\u5185\u81e3", "proof": "F:/untitled2/img/pic_2018_09_20_21_53_23(606635)[mouse0].jpg", "time": "2018/09/20 21:53:23", "children": []}, {"name": "\u90a2\u53f0\u53bf\u90c1\u79cb\u5c0f\u7c73\u52a0", "proof": "F:/untitled2/img/pic_2018_09_20_21_53_18(558363)[mouse0].jpg", "time": "2018/09/20 21:53:18", "children": []}, {"name": "\u4fe1\u534e\u4e3a\u6280\u672f\u6709\u9650\u516c\u53f81\u4fe1\u606f\u5217\u8868", "proof": "F:/untitled2/img/pic_2018_09_20_21_53_05(1340103)[mouse0].jpg", "time": "2018/09/20 21:53:05", "children": []}, {"name": "\u4fe1\u534e\u4e3a\u6280\u672f\u6709\u9650\u516c\u53f81\u4fe1\u606f\u5217\u8868\u00d7\u4fe1\u9ec4\u77f3\u534e\u4e3a\u88c5\u9970\u5de5\u7a0b\u6709\u9650\u516c\u53f8\u4fe1", "proof": "F:/untitled2/img/pic_2018_09_20_21_53_04(1562107)[mouse0].jpg", "time": "2018/09/20 21:53:04", "children": []}, {"name": "\u4fe1\u4e1c\u8425\u534e\u4e3a\u5de5\u7a0b\u9879\u76ee\u7ba1\u7406", "proof": "F:/untitled2/img/pic_2018_09_20_21_53_00(1791103)[mouse0].jpg", "time": "2018/09/20 21:53:00", "children": []}, {"name": "\u4f01\u4e1a\u6cd5\u4eba\u8425\u4e1a\u6267\u7167", "proof": "F:/untitled2/img/pic_2018_09_20_21_52_57(585933)[mouse0].jpg", "time": "2018/09/20 21:52:57", "children": []}, {"name": "\u5e7f\u4e1c\u7701\u6df1\u5733\u5e02\u9f99\u5c97\u533a\u5742\u7530\u8857\u9053\u5c97\u5934\u793e\u533a", "proof": "F:/untitled2/img/pic_2018_09_20_21_52_56(642723)[mouse0].jpg", "time": "2018/09/20 21:52:56", "children": []}, {"name": "\u7535\u4fe1\u8bbe\u5907\u901a\u8baf\u8bbe\u5907", "proof": "F:/untitled2/img/pic_2018_09_20_21_52_55(623657)[mouse0].jpg", "time": "2018/09/20 21:52:55", "children": []}, {"name": "\u5b59\u4e9a\u82b3", "proof": "F:/untitled2/img/pic_2018_09_20_21_52_53(611631)[mouse0].jpg", "time": "2018/09/20 21:52:53", "children": []}, {"name": "\u6df1\u5733\u5e02", "proof": "F:/untitled2/img/pic_2018_09_20_21_52_52(609597)[mouse0].jpg", "time": "2018/09/20 21:52:52", "children": []}]}, {"name": "\u9ec4\u77f3\u534e\u4e3a\u88c5\u9970\u5de5\u7a0b\u6709\u9650\u516c\u53f8", "proof": "F:/untitled2/img/pic_2018_09_20_21_52_31(556499)[mouse0].jpg", "time": "2018/09/20 21:52:31", "children": [{"name": "\u4fe1\u7eff\u76fe\u5168\u56fd\u4f01\u4e1a\u5f81\u4fe1\u7cfb\u7edf", "proof": "F:/untitled2/img/pic_2018_09_20_21_52_44(778105)[mouse0].jpg", "time": "2018/09/20 21:52:44", "children": []}, {"name": "\u4f01\u4e1a\u6cd5\u4eba\u8425\u4e1a\u6267\u7167", "proof": "F:/untitled2/img/pic_2018_09_20_21_52_40(586868)[mouse0].jpg", "time": "2018/09/20 21:52:40", "children": []}, {"name": "\u88c5\u9970\u5de5\u7a0b", "proof": "F:/untitled2/img/pic_2018_09_20_21_52_36(621627)[mouse0].jpg", "time": "2018/09/20 21:52:36", "children": []}, {"name": "\u6e56\u5317\u7701\u9ec4\u77f3\u5e02\u9ec4\u77f3\u6e2f\u533a", "proof": "F:/untitled2/img/pic_2018_09_20_21_52_35(654662)[mouse0].jpg", "time": "2018/09/20 21:52:35", "children": []}]}]}, {"name": "\u4f01\u4e1a\u540d\u79f0\u4fe1\u7528\u7f16\u7801\u6cd5\u5b9a\u4ee3\u8868\u4eba\u80a1\u4e1c\u5931\u4fe1\u88ab\u6267\u884c\u4eba \u534e\u4e3a \u9009\u62e9\u5730\u533a\u641c\u7d22", "proof": "F:/untitled2/img/pic_2018_09_20_21_52_08(1397220)[mouse1].jpg", "time": "2018/09/20 21:52:08", "children": [{"name": "\u4e1c\u8425\u534e\u4e3a\u5de5\u7a0b\u9879\u76ee\u7ba1\u7406\u6709\u9650\u516c\u53f8", "proof": "F:/untitled2/img/pic_2018_09_20_21_52_10(586359)[mouse0].jpg", "time": "2018/09/20 21:52:10", "children": [{"name": "\u4fe1\u7eff\u76fe\u5168\u56fd\u4f01\u4e1a\u5f81\u4fe1\u7cfb\u7edf\u4f01\u4e1a\u4fe1", "proof": "F:/untitled2/img/pic_2018_09_20_21_52_25(602103)[mouse0].jpg", "time": "2018/09/20 21:52:25", "children": []}, {"name": "\u4fe1\u4e1c\u8425\u534e\u4e3a\u5de5\u7a0b\u9879\u76ee\u7ba1\u7406\u6709\u9650\u516c\u4fe1\u4e1c\u8425\u534e\u4e3a\u5de5\u7a0b\u9879\u76ee\u7ba1\u7406\u6709\u9650\u516c\u00d7", "proof": "F:/untitled2/img/pic_2018_09_20_21_52_23(1122111)[mouse0].jpg", "time": "2018/09/20 21:52:23", "children": []}, {"name": "\u4f01\u4e1a\u6cd5\u4eba\u8425\u4e1a\u6267\u7167", "proof": "F:/untitled2/img/pic_2018_09_20_21_52_21(595872)[mouse0].jpg", "time": "2018/09/20 21:52:21", "children": []}, {"name": "\u4e1c\u8425\u533a\u6c82\u6cb3\u8def603\u53f7", "proof": "F:/untitled2/img/pic_2018_09_20_21_52_19(659693)[mouse0].jpg", "time": "2018/09/20 21:52:19", "children": []}, {"name": "\u5c71\u4e1c\u7701\u4e1c\u8425\u5e02\u4e1c\u8425\u533a", "proof": "F:/untitled2/img/pic_2018_09_20_21_52_18(645663)[mouse0].jpg", "time": "2018/09/20 21:52:18", "children": []}, {"name": "\u5de5\u7a0b\u9879\u76ee\u7ba1\u7406\u5de5\u7a0b\u5efa\u8bbe\u76d1\u7406\u5de5\u7a0b\u62db\u3001\u6295\u6807\u4ee3\u7406\u5de5\u7a0b\u9020\u4ef7\u54a8\u8be2\u56ed\u6797\u7eff\u5316\u5de5\u7a0b\u65bd", "proof": "F:/untitled2/img/pic_2018_09_20_21_52_16(646627)[mouse0].jpg", "time": "2018/09/20 21:52:16", "children": []}, {"name": "\u5f90\u5927\u534e", "proof": "F:/untitled2/img/pic_2018_09_20_21_52_14(611598)[mouse0].jpg", "time": "2018/09/20 21:52:14", "children": []}]}]}, {"name": "\u4f01\u4e1a\u540d\u79f0\u4fe1\u7528\u7f16\u7801\u6cd5\u5b9a\u4ee3\u8868\u4eba\u80a1\u4e1c\u5931\u4fe1\u88ab\u6267\u884c\u4eba \u8bf7\u8f93\u5165\u4f01\u4e1a\u540d\u79f0 \u9009\u62e9\u5730\u533a\u641c\u7d22", "proof": "F:/untitled2/img/pic_2018_09_20_21_52_03(1074224)[mouse0].jpg", "time": "2018/09/20 21:52:03", "children": []}, {"name": "\u7eff\u76fe \u641c\u7d22\u4e00\u4e0b", "proof": "F:/untitled2/img/pic_2018_09_20_21_51_56(1235271)[mouse1].jpg", "time": "2018/09/20 21:51:56", "children": []}]}, "name": "\u5f00\u59cb"}}}'
            #print(list_out)
            json_out = json.dumps(list_out)
            # print(json_out)
            response1 = HttpResponse(json_out)
            response1["Access-Control-Allow-Origin"] = "*"
            response1["Access-Control-Allow-Methods"] = "POST,GET,OPTIONS"
            response1["Access-Control-Max-Age"] = "1000"
            response1["Access-Control-Allow-Headers"] = "Origin, X-Requested-With, Content-Type, Accept"
            return response1



def total_getJson(request):
    from data_deal.json1 import makeJson
    import json
    str_out = {'total_json': makeJson('开始', '', '123456')}
    json_out = json.dumps(str_out)
    #json_out = json.loads(json_out)
    response1 = HttpResponse(json_out, content_type='application/json')
    response1["Access-Control-Allow-Origin"] = "*"
    response1["Access-Control-Allow-Methods"] = "POST,GET,OPTIONS"
    response1["Access-Control-Max-Age"] = "1000"
    response1["Access-Control-Allow-Headers"] = "*"
    return response1