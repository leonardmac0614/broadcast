#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
from weather import WeatherPredictData
from BaiduYuyin import YuYin
import DailyEnglish
import itchat

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



if __name__ == '__main__':
    '''
    city id : https://cdn.heweather.com/china-city-list.txt
    灵宝ID：CN101181702
    上海ID：CN101020100
    北京ID：CN101010100
    深圳ID：CN101280601
    长沙ID：CN101250101
    成都ID：CN101270101
    郑州ID：CN101180101
    '''

    cityid = "CN101180101"

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

    result   = YuYin().yuyin(text.encode())



    for i in re:

        print i.decode()
        # itchat.send(i, toUserName='filehelper')
    for i in res:
        print i.decode()
        # itchat.send(i, toUserName='filehelper')
