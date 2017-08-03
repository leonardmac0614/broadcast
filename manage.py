#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
from weather import WeatherPredictData
from BaiduYuyin import YuYin
import DailyEnglish
import json
from email.mime.multipart import MIMEMultipart
#import itchat

'''
每日播报内容：
1.英语早操
2.天气预报
    - 日期、星期、时间
    - 地点
    - 今日天气condition
    - 气温（最高、最低）
    - 空气质量：qlty、pm25、
    - 湿度
    - 风力
    - 建议
        - 穿衣建议
        - 空气建议
        - 紫外线建议
    - 明日预报（condition、最高气温、最低气温）

'''

class Broadcast(object):
    """docstring for Broadcast."""
    def __init__(self):
        return None

    def daily_broadcast(self,cityid):

        data = WeatherPredictData().Output_daily_forecast(cityid)

        return data

    def English_exercise_content(self):

        con= "英语早操："
        en = DailyEnglish.getcontent()[0]
        cn = DailyEnglish.getcontent()[1]

        return [con,en,cn]

    def Client_classification(self):
        '''
        city_id wirte in city_id.json
        '''
        f = open("classify_city_id.json")
        data = json.load(f)
        for k,v in data.items():
            print k,v
        exit()

    def send_message_wechat():
        re = Broadcast().daily_broadcast(cityid)
        res = Broadcast().English_exercise_content()
        text = ""

        for i in re:
            text = text + i

        for i in res:
            text = text + i
        # 登陆
        itchat.auto_login()
        # 发送文本消息，发送目标是“文件传输助手”
        itchat.send(text, toUserName='filehelper')

    def convert_content_for_html(self, cityid):
        re = Broadcast().daily_broadcast(cityid)
        res = Broadcast().English_exercise_content()
        msg      = "<ul>"

        for i in re:
            msg  = msg + "<li>"+str(i.decode())+"</li>"
            # msg  += "</br>"
            # print i.decode()
            # itchat.send(i, toUserName='filehelper')
        msg +="</ul>"
        for i in res:
            msg  += str(i.decode())
            msg  += "</br>"
            # print i.decode()
        return msg

    def convert_content(self, cityid):
        re = Broadcast().daily_broadcast(cityid)
        res = Broadcast().English_exercise_content()
        msg      = ""

        for i in re:
            msg  += str(i.decode())
            msg  += "\n"
            # print i.decode()
            # itchat.send(i, toUserName='filehelper')

        for i in res:
            msg  += str(i.decode())
            msg  += "\n"
            # print i.decode()
        return msg

    def send_message_email_for_html(self, content, _to):
        # 发邮件
        import smtplib
        from email.mime.text import MIMEText

        _user = "147640157@st.usst.edu.cn"
        _pwd  = "q2520457"

        fname = os.path.join("email_template.tpl")
        with open(fname, "r") as tmpl:
            tst = tmpl.read()

        msg = MIMEMultipart()
        msg = MIMEMultipart('alternative')
        msg.attach(MIMEText(tst, 'html', 'utf-8'))

        msg["Subject"] = "每日早操"
        msg["From"]    = _user

        for to in _to:
            msg["To"]      = to
            try:
                s = smtplib.SMTP_SSL("smtp.exmail.qq.com", 465)
                s.login(_user, _pwd)
                s.sendmail(_user, to, msg.as_string())
                s.quit()
                print to + "  Success!"
            except smtplib.SMTPException,e:
                print to + "  Falied,%s"%e



if __name__ == '__main__':

    with open("classify_city_id.json") as cd:
        data = json.load(cd)

    for k,v in data.items():
        print k
        for cityid, _to in v.items():
            if len(_to)>0:
                content = Broadcast().convert_content_for_html(cityid)
                sa      = Broadcast().send_message_email_for_html(content, _to)
            else:
                pass

'''
    re = Broadcast().daily_broadcast(cityid)
    res = Broadcast().English_exercise_content()
    text = ""

    for i in re:
        text = text + i

    for i in res:
        text = text + i

    # 登陆
    # itchat.auto_login()
    # 发送文本消息，发送目标是“文件传输助手”
    # itchat.send(text, toUserName='filehelper')

    result   = YuYin().yuyin(text.encode())
    msg      = ""


    for i in re:
        msg  += str(i.decode())
        msg  += "\n"
        # print i.decode()
        # itchat.send(i, toUserName='filehelper')
    for i in res:
        msg  += str(i.decode())
        msg  += "\n"
        # print i.decode()

    # itchat.send(msg, toUserName='filehelper')

    # 发邮件
    import smtplib
    from email.mime.text import MIMEText

    _user = "147640157@st.usst.edu.cn"
    _pwd  = "q2520457"
    _to   = ["405666135@qq.com","shuailong_li@163.com","673842584@qq.com"]

    msg = MIMEText(msg)
    msg["Subject"] = "每日早操"
    msg["From"]    = _user

    for to in _to:
        msg["To"]      = to
        try:
            s = smtplib.SMTP_SSL("smtp.exmail.qq.com", 465)
            s.login(_user, _pwd)
            s.sendmail(_user, to, msg.as_string())
            s.quit()
            print "Success!"
        except smtplib.SMTPException,e:
            print "Falied,%s"%e
'''
