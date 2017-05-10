# coding=utf-8
import urllib2
import json



'''
json格式: https://api.heweather.com/x3/weather?cityid=CN101181702&key=8cc5c90533674084ab4f84d6227b7bc2

city id : https://cdn.heweather.com/china-city-list.txt
灵宝ID：CN101181702
上海ID：CN101020100
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

        ata           = self.get_data_from_heweather(cityid)
        suggestion = data["HeWeather data service 3.0"][0]["suggestion"]

        return suggestion

    def Output_daily_forecast(self,cityid):

        '''
        每日播报内容：
        1.英语早操（todo：英文语音。done：中文语音）
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




if __name__ == '__main__':

    data = WeatherPredictData().Heweather_daily_forecast("CN101181702")

    print data
