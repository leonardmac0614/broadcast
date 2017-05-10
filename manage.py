#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from weather import WeatherPredictData
from BaiduYuyin import YuYin


class Broadcast(object):
    """docstring for Broadcast."""
    def __init__(self):
        

        return None


    def daily_broadcast(self,cityid):



        weatherdata = WeatherPredictData().Heweather_daily_forecast(cityid)

        return weatherdata



if __name__ == '__main__':

    cityid = "CN101181702"

    re = Broadcast().daily_broadcast(cityid)

    print re
