#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import urllib2
import json



'''
json格式: https://api.heweather.com/x3/weather?cityid=CN101181702&key=8cc5c90533674084ab4f84d6227b7bc2

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
        self.url = "https://api.heweather.com/x3/weather?cityid=%s&key=8cc5c90533674084ab4f84d6227b7bc2"
    def get_data_from_heweather(self,cityid):

        url = self.url % cityid
        req = urllib2.Request(url)
        resp = urllib2.urlopen(req).read()
        data = json.loads(resp)

        weather = data["HeWeather data service 3.0"]
        daily_forecast = weather[0]["daily_forecast"]
        aqi            = weather[0]["aqi"]
        basic          = weather[0]["basic"]
        hourly_forecast= weather[0]["hourly_forecast"]
        suggestion     = weather[0]["suggestion"]
        return data

    def Heweather_basic(self,cityid):

        data = self.get_data_from_heweather(cityid)
        basic = data["HeWeather data service 3.0"][0]["basic"]
        return basic

    def Heweather_daily_forecast(self,cityid):

        data           = self.get_data_from_heweather(cityid)
        daily_forecast = data["HeWeather data service 3.0"][0]["daily_forecast"]

        return daily_forecast

    def Heweather_aqi(self, cityid):

        data           = self.get_data_from_heweather(cityid)
        aqi = data["HeWeather data service 3.0"][0]["aqi"]

        return aqi

    def Heweather_hourly_forecast(self, cityid):

        data           = self.get_data_from_heweather(cityid)
        hourly_forecast = data["HeWeather data service 3.0"][0]["hourly_forecast"]

        return hourly_forecast

    def Heweather_suggestion(self, cityid):

        data           = self.get_data_from_heweather(cityid)
        suggestion = data["HeWeather data service 3.0"][0]["suggestion"]

        return suggestion

    def Output_daily_forecast(self,cityid):

        city_name        = self.Heweather_basic(cityid)["city"]
        latest_data_date = "最新天气更新时间："+self.Heweather_basic(cityid)["update"]["loc"]
        condition_day    = "白天：" + self.Heweather_daily_forecast(cityid)[0]["cond"]["txt_d"]+"."
        condition_night  = "夜间：" + self.Heweather_daily_forecast(cityid)[0]["cond"]["txt_n"]+"."
        humidity         = "湿度：" + self.Heweather_daily_forecast(cityid)[0]["hum"]+ "%"
        temperature_max  = "最高温度：" + self.Heweather_daily_forecast(cityid)[0]["tmp"]["max"]+"℃"
        temperature_min  = "最低温度：" + self.Heweather_daily_forecast(cityid)[0]["tmp"]["min"]+"℃"
        wind             = self.Heweather_daily_forecast(cityid)[0]["wind"]["dir"]+ " 风速：" + self.Heweather_daily_forecast(cityid)[0]["wind"]["spd"]+"km/h"
        suggestion_air   = "天气建议:" + self.Heweather_suggestion(cityid)["air"]["txt"]
        suggestion_comf  = "舒适度：" + self.Heweather_suggestion(cityid)["comf"]["txt"]
        suggestion_drsg  = "穿衣建议：" + self.Heweather_suggestion(cityid)["drsg"]["txt"]
        suggestion_sport = "运动建议：" + self.Heweather_suggestion(cityid)["sport"]["txt"]

        return[city_name,latest_data_date,condition_day,condition_night,humidity,temperature_max,temperature_min,wind,suggestion_air,suggestion_comf,suggestion_drsg,suggestion_sport]




if __name__ == '__main__':
    data = []

    data = WeatherPredictData().Output_daily_forecast("CN101181702")
    # print data
    # for i in data:

        # print i.decode()
