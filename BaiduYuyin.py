#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import urllib2
import urllib
import webbrowser

'''
https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=vrikaaMUSknn1izjXZk1NuF9&client_secret=47b647223883e2cb625b6b6446cd3961

https://openapi.baidu.com/oauth/2.0/token?
    grant_type=client_credentials&
    client_id=vrikaaMUSknn1izjXZk1NuF9&
    client_secret= 47b647223883e2cb625b6b6446cd3961&

acess_token =  24.6ed051e0ba2b1fe944da549846a4b39d.2592000.1499854092.282335-9750820
'''
class YuYin(object):
    """docstring for yuyin."""
    def __init__(self):

        return None

    def yuyin(self,text):

        url  = "http://tsn.baidu.com/text2audio?tex=%s&lan=zh&per=0&cuid=98:01:a7:b0:90:23&ctp=1&tok=24.6ed051e0ba2b1fe944da549846a4b39d.2592000.1499854092.282335-9750820"
        text = urllib.quote(text)
        url  = url % text

        webbrowser.open(url)
        return url

if __name__ == '__main__':
    text = "大撒的见风使舵了房间"
    re   = YuYin().yuyin(text)
