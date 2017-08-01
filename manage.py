#!/usr/bin/env python
# -*- coding: utf-8 -*-
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

    def send_message_email_for_html(self, cityid, _to):
        # 发邮件
        import smtplib
        from email.mime.text import MIMEText
        content   = Broadcast().convert_content_for_html(cityid)

        _user = "147640157@st.usst.edu.cn"
        _pwd  = "q2520457"
        # _to   = ["405666135@qq.com","shuailong_li@163.com"]
        # "673842584@qq.com"

        tst ='''
        <html><body>
        <div class="email-body" style="box-sizing: border-box; color: #383838; font-family: 'Helvetica Neue', 'Hiragino Sans GB', 'WenQuanYi Micro Hei', 'Microsoft Yahei', sans-serif; font-size: 14px; line-height: 1.42857143; max-width: 708px; min-height: 100%; background: #FFFFFF; margin: 0 auto; padding: 30px;">
                <div class="table-wrap" style="box-sizing: border-box; clear: both; display: block; font-family: 'Helvetica Neue', 'Hiragino Sans GB', 'WenQuanYi Micro Hei', 'Microsoft Yahei', sans-serif; font-size: 14px; line-height: 1.42857143; width: 690px; background: #FFFFFF; margin: 0 auto; padding: 0;">
                    <table class="body-wrap" style="border-collapse: collapse; box-sizing: border-box; font-family: 'Helvetica Neue', 'Hiragino Sans GB', 'WenQuanYi Micro Hei', 'Microsoft Yahei', sans-serif; font-size: 14px; line-height: 1.42857143; width: 100%; margin: 0; padding: 0; border: 0;">
        <tbody><tr style="box-sizing: border-box; font-family: 'Helvetica Neue', 'Hiragino Sans GB', 'WenQuanYi Micro Hei', 'Microsoft Yahei', sans-serif; font-size: 14px; line-height: 1.42857143; margin: 0; padding: 0;">
        <td valign="top" style="border-radius: 6px; box-sizing: border-box; color: #A6A6A6; display: block; font-family: Helvetica Neue Light,Helvetica Neue,Hiragino Sans GB,Microsoft Yahei,Trebuchet MS,Arial; font-size: 16px; font-weight: normal; letter-spacing: normal; line-height: 40px; text-align: center; vertical-align: top; background: #FFFFFF; margin: 0; padding: 0 0 25px;" align="center" bgcolor="#FFFFFF"><img src="https://ooo.0o0.ooo/2017/06/15/59421bfcb771d.png" style="box-sizing: border-box; font-family: 'Helvetica Neue', 'Hiragino Sans GB', 'WenQuanYi Micro Hei', 'Microsoft Yahei', sans-serif; font-size: 14px; line-height: 1.42857143; max-width: 100%; vertical-align: middle; width: 158px; margin: 0; padding: 0;"></td>
                        </tr>
        <tr style="box-sizing: border-box; font-family: 'Helvetica Neue', 'Hiragino Sans GB', 'WenQuanYi Micro Hei', 'Microsoft Yahei', sans-serif; font-size: 14px; line-height: 1.42857143; margin: 0; padding: 0;">
        <td class="container" style="border-radius: 5px; box-sizing: border-box; font-family: 'Helvetica Neue', 'Hiragino Sans GB', 'WenQuanYi Micro Hei', 'Microsoft Yahei', sans-serif; font-size: 14px; line-height: 1.42857143; vertical-align: top; width: 100%; background: #FFFFFF; margin: 0; padding: 30px 40px; border: 1px solid #d9d9d9;" bgcolor="#FFFFFF" valign="top">
                                <div style="box-sizing: border-box; font-family: 'Helvetica Neue', 'Hiragino Sans GB', 'WenQuanYi Micro Hei', 'Microsoft Yahei', sans-serif; font-size: 14px; line-height: 1.42857143; margin: 0; padding: 0;">
                                    <table style="border-collapse: collapse; box-sizing: border-box; font-family: 'Helvetica Neue', 'Hiragino Sans GB', 'WenQuanYi Micro Hei', 'Microsoft Yahei', sans-serif; font-size: 14px; line-height: 1.42857143; width: 100%; margin: 0; padding: 0; border: 0;"><tbody><tr style="box-sizing: border-box; font-family: 'Helvetica Neue', 'Hiragino Sans GB', 'WenQuanYi Micro Hei', 'Microsoft Yahei', sans-serif; font-size: 14px; line-height: 1.42857143; margin: 0; padding: 0;">
        <td style="box-sizing: border-box; font-family: 'Helvetica Neue', 'Hiragino Sans GB', 'WenQuanYi Micro Hei', 'Microsoft Yahei', sans-serif; font-size: 14px; line-height: 1.42857143; vertical-align: top; margin: 0; padding: 0;" valign="top">
                                                <table id="content" cellspacing="0" cellpadding="0" border="0" style="border-collapse: collapse; box-sizing: border-box; font-family: 'Helvetica Neue', 'Hiragino Sans GB', 'WenQuanYi Micro Hei', 'Microsoft Yahei', sans-serif; font-size: 14px; line-height: 1.42857143; width: 100%; margin: 0; padding: 0; border: 0;">
        <tbody><tr style="box-sizing: border-box; font-family: 'Helvetica Neue', 'Hiragino Sans GB', 'WenQuanYi Micro Hei', 'Microsoft Yahei', sans-serif; font-size: 14px; line-height: 1.42857143; margin: 0; padding: 0;">
        <td valign="top" style="border-radius: 6px; box-sizing: border-box; color: #A6A6A6; display: block; font-family: Helvetica Neue Light,Helvetica Neue,Hiragino Sans GB,Microsoft Yahei,Trebuchet MS,Arial; font-size: 16px; font-weight: normal; letter-spacing: normal; line-height: 40px; text-align: center; vertical-align: top; background: #FFFFFF; margin: 0; padding: 0 0 40px;" align="center" bgcolor="#FFFFFF"><img src="https://ooo.0o0.ooo/2017/06/15/59421d870314d.png" style="box-sizing: border-box; font-family: 'Helvetica Neue', 'Hiragino Sans GB', 'WenQuanYi Micro Hei', 'Microsoft Yahei', sans-serif; font-size: 14px; line-height: 1.42857143; max-width: 100%; vertical-align: middle; width: 173px; margin: 0; padding: 0;"></td>
                                                    </tr>
        <tr style="box-sizing: border-box; font-family: 'Helvetica Neue', 'Hiragino Sans GB', 'WenQuanYi Micro Hei', 'Microsoft Yahei', sans-serif; font-size: 14px; line-height: 1.42857143; margin: 0; padding: 0;">
        <td style="box-sizing: border-box; font-family: 'Helvetica Neue', 'Hiragino Sans GB', 'WenQuanYi Micro Hei', 'Microsoft Yahei', sans-serif; font-size: 14px; line-height: 1.42857143; vertical-align: top; margin: 0; padding: 0;" valign="top">
                                                            <div class="content" style="box-sizing: border-box; font-family: 'Helvetica Neue', 'Hiragino Sans GB', 'WenQuanYi Micro Hei', 'Microsoft Yahei', sans-serif; font-size: 14px; line-height: 1.42857143; margin: 0; padding: 0;">
        <p>Hi，早上好！</p>
        <p>新的一天已经开始，让我们一起嗨起来！</p>'''+content+'''

        <p><br></p>
        </div>
                                                        </td>
                                                    </tr>

        <tr style="box-sizing: border-box; font-family: 'Helvetica Neue', 'Hiragino Sans GB', 'WenQuanYi Micro Hei', 'Microsoft Yahei', sans-serif; font-size: 14px; line-height: 1.42857143; margin: 0; padding: 0;">

                                                        </td>


                                                        <td style="box-sizing: border-box; font-family: 'Helvetica Neue', 'Hiragino Sans GB', 'WenQuanYi Micro Hei', 'Microsoft Yahei', sans-serif; font-size: 14px; line-height: 1.42857143; vertical-align: top; margin: 0; padding: 0;" valign="top"></td>
                                                        </tr></tbody></table>
        </td>
                                            </tr>
        <tr style="box-sizing: border-box; font-family: 'Helvetica Neue', 'Hiragino Sans GB', 'WenQuanYi Micro Hei', 'Microsoft Yahei', sans-serif; font-size: 14px; line-height: 1.42857143; margin: 0; padding: 0;">
        <td style="box-sizing: border-box; font-family: 'Helvetica Neue', 'Hiragino Sans GB', 'WenQuanYi Micro Hei', 'Microsoft Yahei', sans-serif; font-size: 14px; line-height: 1.42857143; vertical-align: top; margin: 0; padding: 0;" valign="top">
                                                    <p style="box-sizing: border-box; font-family: 'Helvetica Neue', 'Hiragino Sans GB', 'WenQuanYi Micro Hei', 'Microsoft Yahei', sans-serif; font-size: 14px; font-weight: normal; line-height: 1.42857143; text-align: center; margin: 0 0 10px; padding: 0;" align="center">我可以接受失败，但我绝不能接受我都未曾奋斗过！</p>
                                                    <p align="center"><a href="http://www.leonardmac.me" target="_blank" style="box-sizing: border-box; color: #03A9F4; font-family: 'Helvetica Neue', 'Hiragino Sans GB', 'WenQuanYi Micro Hei', 'Microsoft Yahei', sans-serif; font-size: 14px; line-height: 1.42857143; text-decoration: none; margin: 0; padding: 0;">李二狗的妖孽人生</a></p>
                                                </td>
                                            </tr>
        </tbody></table>
        </td>
                            </tr></tbody></table>
        </div>
                            </td>
                            <td style="box-sizing: border-box; font-family: 'Helvetica Neue', 'Hiragino Sans GB', 'WenQuanYi Micro Hei', 'Microsoft Yahei', sans-serif; font-size: 14px; line-height: 1.42857143; vertical-align: top; margin: 0; padding: 0;" valign="top"></td>
                        </tr>
        </tbody></table>
        </div>
            </div>
        </body></html>
        '''

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
    '''
    cityid = "CN101200101"
    _to   = ["junling.gao@midea.com.cn"]
    sa    = Broadcast().send_message_email(cityid, _to)

    exit()
    '''

    f = open("/root/broadcast/classify_city_id.json")
    data = json.load(f)
    for k,v in data.items():
        print k
        for cityid, _to in v.items():
            if len(_to)>0:
                sa    = Broadcast().send_message_email_for_html(cityid, _to)
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
