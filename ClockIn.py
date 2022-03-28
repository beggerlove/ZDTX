# encoding=utf-8
import json
import random
import sys
import time
from hashlib import md5
from urllib import parse

import requests
import urllib3

urllib3.disable_warnings()

# --------------------------------------------------------------------------
phone = sys.argv[1]
pwd = sys.argv[2]
address = sys.argv[3]
lat = sys.argv[4]
lng = sys.argv[5]
district = sys.argv[6]
deviceToken = sys.argv[7]
pushplus = sys.argv[8]
# ---------------------------------------------------------------------------
session = requests.Session()
now = time.time() + 28800
date = time.strftime("%m{month}%d{day}", time.localtime(now)).format(month='月', day='日')

# Push
def Push(msg, template=""):
    print("推送消息:[", parse.unquote(msg), ']')
    PushPlus(msg, template)

# PushPlus推送
def PushPlus(msg, template=""):
    url = f'https://www.pushplus.plus/send?token={pushplus}&title={date}{"指点天下梦中打卡"}&content={msg}{template}'
    try:
        requests.post(url)
    except:
        pass


# 指点天下登录模块
def login():
    url = 'http://app.zhidiantianxia.cn/api/Login/pwd'
    encoded_pwd = md5('axy_{}'.format(pwd).encode()).hexdigest()
    global flag
    header = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '201',
        'Host': 'app.zhidiantianxia.cn',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/3.10.0'
    }
    data = {
        'phone': phone,
        'password': encoded_pwd,
        'mobileSystem': '12',
        'appVersion': '1.7.3',
        'mobileVersion': 'PDSM00',
        'deviceToken': deviceToken,
        'pushToken': phone,
        'romInfo': 'OPPO',
    }

    response = session.post(url=url, headers=header, data=data)
    if response.json()['status'] == 1:
        print('登录成功')
        flag = 1
    else:
        print(response.json()['msg'])
        msg = parse.quote_plus(response.json()['msg'])
        Push(msg)
        flag = 0
    return response.json()['data']


# 获取打卡信息模板ID
def get_templateID(token):
    url = 'http://zzcsjr.zhidiantianxia.cn/api/study/health/mobile/health/permission'
    header = {
        'axy-phone': phone,
        'axy-token': token,
        'user-agent': 'PDSM00(Android/12) (com.axy.zhidian/1.7.3) Weex/0.18.0 1080x2293',
        'Host': 'zzcsjr.zhidiantianxia.cn',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
    }
    response = session.get(url=url, headers=header)
    if response.status_code == 200:
        if response.json()['status'] == 1:
            template_id = response.json()['data']['templateId']
            isSubmitted = response.json()['data']['submitted']
            print("获取模板ID成功,模板ID为:", template_id, end='\n')
            return template_id, isSubmitted
        else:
            print("登录错误!")
            return -1

        
# 获取模板
def get_template(token, template_id):
    url = 'http://zzcsjr.zhidiantianxia.cn/api/study/health/mobile/health/template?id={}'.format(template_id)
    header = {
        'axy-phone': phone,
        'axy-token': token,
        'user-agent': 'PDSM00(Android/12) (com.axy.zhidian/1.7.3) Weex/0.18.0 1080x2293',
        'Host': 'zua.zhidiantianxia.cn',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
    }
    response = session.get(url=url, headers=header)
    type(response.json)
    # print('模板\n', response.json())
    return response.json()

def parse_template(template, templateId):
    template = template['data']
    c = 1
    summary = "模板ID" + str(templateId) + "\n"
    try:
        for i__ in template:
            if isinstance(i__,dict):
                if 'optionSelected' in i__:
                    for item in i__['optionSelected'][0]['fields']:
                        summary = summary + '    ' + '- ' + item['fieldTitle'] + '\n'
                summary = summary + str(c) + '.' + i__['fieldTitle'] + '\n'
                c = c + 1
    except:
        print("解析失败，但不影响打卡！\n")
    return summary

        

# 随机体温
def random_temperature():
    return str(round(random.uniform(36.2, 36.8), 1))


# 每日健康打卡模块
def sign_in(token):
    url = 'http://zzcsjr.zhidiantianxia.cn/api/study/health/apply'
    header = {
        'axy-phone': phone,
        'axy-token': token,
        'Content-Type': 'application/json',
        'user-agent': 'PDSM00(Android/12) (com.axy.zhidian/1.7.3) Weex/0.18.0 1080x2293',
        'Host': 'zzcsjr.zhidiantianxia.cn',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'Content-Length': '695'
    }

    content = {
        "location": {"address": address, "code": "1", "lng": lng, "lat": lat},
        "temperature": random_temperature(),
        "health": "是",
        "observation": "否",
        "confirmed": "否",
        "haveCOVIDInPlaceOfAbode": "否",
        "goToHuiBei": "否",
        "contactIllPerson": "否",
        "haveYouEverBeenAbroad": "否",
        "familyPeopleNum": "4",
        "isFamilyHealth": "否",
        "isFamilyStatus": "否",
        "familyPeopleIsAway": "否",
        "hasYourFamilyEverBeenAbroad": "否",
        "leave": "否",
        "isYesterdayMove": "否",
        "admission": "是",
        "help": "否",
        "nowLocation": district
    }

    data = {
        "health": 0,
        "student": 1,
        "templateId": 4,
        "content": str(content)
    }
    template_id, isSubmitted = get_templateID(token)
    print(template_id, isSubmitted)
    time.sleep(3)
    template = (get_template(token, template_id))
    tttt = parse_template(template, template_id)
    time.sleep(2)
    data = json.dumps(data)
    response = session.post(url=url, headers=header, data=data)
    if response.json()['status'] == 1:
        msg = response.json()['msg'] + f'\n当前模板ID为{template_id}'  # 打卡成功
        Push(msg, tttt)
        print(tttt)
    else:
        msg = parse.quote_plus(response.json()['msg'])
        Push(msg, tttt)
        print(tttt)
        print(parse.unquote(msg))
        
        
        
        

# 获取每日宿舍签到的signInId模块
def get_signInId(token):
    url = 'http://zzcsjr.zhidiantianxia.cn/applets/signin/my'
    header = {
        'axy-phone': phone,
        'axy-token': token,
        'user-agent': 'PDSM00(Android/12) (com.axy.zhidian/1.7.3) Weex/0.18.0 1080x2293',
        'Host': 'zzcsjr.zhidiantianxia.cn',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip'
    }
    data = {
        'page': '0',
        'size': '10'
    }
    try:
        signInId = session.get(url=url, headers=header, data=data).json()['data']['content'][0]['id']
        return signInId
    except:
        pass


# 22点宿舍签到模块
def sign_in_evening(token):
    url = 'http://zzcsjr.zhidiantianxia.cn/applets/signin/sign'
    header = {
        'axy-phone': phone,
        'axy-token': token,
        'Content-Type': 'application/json',
        'user-agent': 'PDSM00(Android/12) (com.axy.zhidian/1.7.3) Weex/0.18.0 1080x2293',
        'Host': 'zzcsjr.zhidiantianxia.cn',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'Content-Length': '146'
    }
    data = {
        "locale": address,
        "lat": lat,
        "lng": lng,
        "signInId": get_signInId(token)
    }
    data = json.dumps(data)
    response = session.post(url=url, headers=header, data=data)
    if response.json()['status'] == 1:
        print("签到成功")
    else:
        print("签到失败")
    msg = parse.quote_plus(response.json()['msg'])
    Push(msg)


if __name__ == "__main__":
    token = login()
    time.sleep(3)
    now_H = int(time.strftime("%H"))
    if flag == 1:
        if 14 <= now_H <= 15:  # 世界协调时间
            sign_in_evening(token)
        else:
            sign_in(token)
    else:
        pass
