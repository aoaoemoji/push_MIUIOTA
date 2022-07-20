# -*- coding: utf-8 -*-
# @Author: aoao
# @Date:   2022-06-10 09:09:34
# @Last Modified by:   aoao
# @Last Modified time: 2022-06-15 17:49:23

import urllib.request
import urllib.parse
import json
import urllib.error
from lxml import etree
import os
import time
from datetime import datetime, date

def getnewROM(send):
    try:
        send = urllib.parse.quote(send)
        url = "TGAPI密匙填写在这里/sendMessage?chat_id=@fiimerom&text=" + send  # 注意改个密匙
        headers = {
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Mobile Safari/537.36'
        }
        request = urllib.request.Request(url=url,headers=headers)
        reponse = urllib.request.urlopen(request)
    except:
        pass



dayOfWeek = datetime.now().weekday()
if dayOfWeek in [0,1,2,3]:
    ppppp = "1"
elif dayOfWeek in [4]:
    ppppp = "1b"
else:
    print('今天是非工作日!跳过')
    exit()


getnewROM('FiimeROM提示：检测到MIUI更新，推送1分钟后开始')
time.sleep(60)

# 接口地址
url = "https://miui.511i.cn/?index=rom_list"
headers = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Mobile Safari/537.36'
}
# vab机型数据
d = ['ALIOTH','ODIN','RUBENS','MATISSE','INGRES','MONA','ELISH','HAYDN','PSYCHE','RENOIR','STAR','THYME','VENUS','APOLLO','CAS','CUPID','ZEUS','PSYCHE','XAGA','ZIJIN']
n = 0
for a in d:
    data = {
        'dh':a,
         # lx参数: 0稳定版,1开发版内测,1b开发版公测
        'lx':ppppp
    }
    data = urllib.parse.urlencode(data).encode("utf-8")
    if a == 'ALIOTH':
        name = '红米K40 / POCO F3'
    elif a == 'ODIN':
        name = '小米MIX4'
    elif a == 'RUBENS':
        name = '红米K50' 
    elif a == 'MATISSE':
        name = '红米K50 Pro' 
    elif a == 'INGRES':
        name = '红米K50 电竞版'
    elif a == 'MONA':
        name = '小米CIVI'
    elif a == 'ELISH':
        name = '小米平板5 Pro (WiFi)'
    elif a == 'HAYDN':
        name = '红米K40 Pro系列'
    elif a == 'PSYCHE':
        name = '小米12X'
    elif a == 'RENOIR':
        name = '小米11 青春版'
    elif a == 'STAR':
        name = '小米11 Pro / Ultra'
    elif a == 'THYME':
        name = '小米10S'
    elif a == 'VENUS':
        name = '小米11'
    elif a == 'APOLLO':
        name = '红米K30S 至尊纪念版'
    elif a == 'CAS':
        name = '小米10 UITra'
    elif a == 'CUPID':
        name = '小米12'
    elif a == 'ZEUS':
        name = '小米12 Pro'
    elif a == 'PSYCHE':
        name = '小米12X'
    elif a == 'XAGA':
        name = '红米Note11T Pro / Pro+'
    elif a == 'ZIJIN':
        name = '小米CIVI 1S'
    try:
        request = urllib.request.Request(url=url,data=data,headers=headers)
        reponse = urllib.request.urlopen(request)
        contant = etree.HTML(reponse.read().decode("utf-8"))
        list_td = contant.xpath("//td//a[@href]/@href")
        today = datetime.today().strftime('%Y-%m-%d')
        try:
            # print(list_td[0]) 获取最新的一个内测版本地址
            # getnewROM("获取到更新:代号【" + a + "】\n下载地址:" + str(list_td[0]))
            if str(list_td[0]) == '':
                pass
            else:
                n += 1
                getnewROM("获取到第" + str(n) + "个更新：\n机型：" + name + "\n代号：【" + a + "】\n发布时间：" + today + "\n下载地址：\n" + str(list_td[0]))
                with open('/www/wwwroot/mi.fiime.cn/0相关资料/sql.txt','a') as f:
                    f.write(str(list_td[0])+'\n')
        except Exception as e:
            print(e)
            continue
    except urllib.error.HTTPError:
        print('网络错误，获取异常！')
    except urllib.error.URLError:
        print('当前%sROM无有效链接！'%(a))

getnewROM('今日获取MIUI更新结束！\n 技术支持: https://mi.fiime.cn')