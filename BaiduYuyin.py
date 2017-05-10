#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import urllib2
import urllib
import webbrowser

'''
https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=9623067&client_secret=wUR5f0xwBZ2Bd3XhduhMyyYH

https://openapi.baidu.com/oauth/2.0/token?
    grant_type=client_credentials&
    client_id=wUR5f0xwBZ2Bd3XhduhMyyYH&
    client_secret= 39bee0c637f30f47c09bd78897faedc9&

acess_token =  23.be37b6d551b92aabe2831ff3c034e493.2592000.1496912910.2400369472-9623067
'''
class YuYin(object):
    """docstring for yuyin."""
    def __init__(self):

        return None

    def yuyin(self,text):

        url  = "http://tsn.baidu.com/text2audio?tex=%s&lan=zh&per=0&cuid=98:01:a7:b0:90:23&ctp=1&tok=23.be37b6d551b92aabe2831ff3c034e493.2592000.1496912910.2400369472-9623067"
        text = urllib.quote(text)
        url  = url % text

        webbrowser.open(url)
        return url

if __name__ == '__main__':
    text = "大撒的见风使舵了房间"
    re   = YuYin().yuyin(text)
