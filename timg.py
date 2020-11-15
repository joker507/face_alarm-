# -*- coding: utf-8 -*-
import datetime
import time
from datetime import datetime
import requests
import main
import towav


#获取本地时间
def get_loc_time():
    tz = pytz.timezone('Asia/Shanghai') #东八区
    t = datetime.fromtimestamp(int(time.time()),
        pytz.timezone('Asia/Shanghai')).strftime('%H:%M')
    print(t)    # ==> 2017-12-05 18:39:45 CST+0800
    return t

#获取北京网络时间
def getBeijinTime():
    try:
        # 设置头信息，没有访问会错误400！！！
        hea = {'User-Agent': 'Mozilla/5.0'}
        # 设置访问地址，我们分析到的；
        url = r'http://time1909.beijing-time.org/time.asp'
        # 用requests get这个地址，带头信息的；
        r = requests.get(url=url,headers=hea)
        # 检查返回的通讯代码，200是正确返回；

        if r.status_code == 200:
            # 定义result变量存放返回的信息源码；
            result = r.text
            # 通过;分割文本；
            data = result.split(";")
            # print("data:",data)
            # ======================================================
            # 以下是数据文本处理：切割、取长度，最最基础的东西就不描述了；
            year = data[1][len("nyear") + 3: len(data[1])]
            month = data[2][len("nmonth") + 3: len(data[2])]
            day = data[3][len("nday") + 3: len(data[3])]
            hrs = data[5][len("nhrs") + 3: len(data[5])]
            minute = data[6][len("nmin") + 3: len(data[6])]
            sec = data[7][len("nsec") + 3: len(data[7])]
            # ======================================================
            # 这个也简单把切割好的变量拼到beijinTimeStr变量里；
            # beijinTimeStr = "%s/%s/%s %s:%s:%s" % (year, month, day, hrs, minute, sec)
            beijinTimeStr = "%s:%s" % (hrs, minute)
            # 把时间打印出来看看；
            # print(beijinTimeStr)
            # 将beijinTimeStr转为时间戳格式；
            # beijinTime = time.mktime(time.strptime(beijinTimeStr, "%Y/%m/%d %X"))
            # #返回时间戳；
        return (beijinTimeStr)
    except:
        #没有网络情况获取本机时间
        beijinTimeStr = get_loc_time()

        return beijinTimeStr

#获取定时时间
def get_timg():
    towav.note() #过去网站时间保存到test1.txt文件
    with open("test1.txt",'r') as f:
        timg = f.read()
    return timg

#循环匹配
t = getBeijinTime()
print(t)
timg=get_timg()
print(timg)
print("timg:",timg)
while 1:
    timg=get_timg() #获取定时时间
    t = getBeijinTime() #获取北京时间
    print("timg:", timg)
    if timg == t: #匹配
        main.main()
        time.sleep(50)
    time.sleep(10)
    print('t:',t)