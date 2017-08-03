#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import urllib2
import json



'''
json格式: https://free-api.heweather.com/v5/weather?city=CN101181702&key=8cc5c90533674084ab4f84d6227b7bc2

city id : https://cdn.heweather.com/china-city-list.txt
灵宝ID：CN101181702
上海ID：CN101020100
北京ID：CN101010100
深圳ID：CN101280601
'''
class WeatherPredictData(object):
    """docstring for Weather."""

    def __init__(self):

        # %s city id
        self.url = "https://free-api.heweather.com/v5/weather?city=%s&key=8cc5c90533674084ab4f84d6227b7bc2"

    def get_data_from_heweather(self,cityid):

        url = self.url % cityid
        req = urllib2.Request(url)
        resp = urllib2.urlopen(req).read()
        data = json.loads(resp)

        return data

    def Heweather_basic(self, data):

        basic = data["HeWeather5"][0]["basic"]
        return basic

    def Heweather_daily_forecast(self, data):

        daily_forecast = data["HeWeather5"][0]["daily_forecast"]

        return daily_forecast

    def Heweather_aqi(self, data):

        aqi = data["HeWeather5"][0]["aqi"]

        return aqi

    def Heweather_hourly_forecast(self, data):

        hourly_forecast = data["HeWeather5"][0]["hourly_forecast"]

        return hourly_forecast

    def Heweather_suggestion(self, data):

        suggestion = data["HeWeather5"][0]["suggestion"]

        return suggestion

    def Output_daily_forecast(self,cityid):
        data             = self.get_data_from_heweather(cityid)
        city_name        = self.Heweather_basic(data)["city"]
        latest_data_date = city_name + "最新天气更新时间："+self.Heweather_basic(data)["update"]["loc"]
        condition_day    = "白天：" + self.Heweather_daily_forecast(data)[0]["cond"]["txt_d"]+"."
        condition_night  = "夜间：" + self.Heweather_daily_forecast(data)[0]["cond"]["txt_n"]+"."
        humidity         = "湿度：" + self.Heweather_daily_forecast(data)[0]["hum"]+ "%"
        temperature_max  = "最高温度：" + self.Heweather_daily_forecast(data)[0]["tmp"]["max"]+"℃"
        temperature_min  = "最低温度：" + self.Heweather_daily_forecast(data)[0]["tmp"]["min"]+"℃"
        wind             = self.Heweather_daily_forecast(data)[0]["wind"]["dir"]+ " 风速：" + self.Heweather_daily_forecast(data)[0]["wind"]["spd"]+"km/h"
        suggestion_air   = "天气建议: " + self.Heweather_suggestion(data)["air"]["txt"]
        suggestion_comf  = "舒适度：" + self.Heweather_suggestion(data)["comf"]["txt"]
        suggestion_drsg  = "穿衣建议：" + self.Heweather_suggestion(data)["drsg"]["txt"]
        suggestion_sport = "运动建议：" + self.Heweather_suggestion(data)["sport"]["txt"]

        return[latest_data_date,condition_day,condition_night,humidity,temperature_max,temperature_min,wind,suggestion_air,suggestion_comf,suggestion_drsg,suggestion_sport]




if __name__ == '__main__':
    data = []

    data = WeatherPredictData().Output_daily_forecast("CN101181702")

    for i in data:

        print i.decode()
