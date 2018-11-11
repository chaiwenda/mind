# 间隔0.1秒 调用一次函数
# 如果有信号过来将delay_time的值修改，则不执行
import time

def sleeptime(hour,min,sec):
    return hour*3600 + min*60 + sec
second = sleeptime(0,0,0.1)
delay_time = True
i = 1
while i > 0 :
    i = i + 1
    if i == 180 or i == 1800 or i == 1900:
        delay_time = False
    if delay_time == True:
        time.sleep(second)
        print('实时刷新页面内容')
    else:
        delay_time = True
        print("暂时不刷新页面内容")