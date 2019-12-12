#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import urllib2
import urllib
import webbrowser

'''
https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=2HIvTvqXc4cX6iaEsSytvDE9&client_secret=cd8ZA1dn6oICbLb3EgaaEpmUyiLQHGGh

{
    "access_token": "24.b8068162e54151bfdaf05da4151bc056.2592000.1516451144.282335-10567712",
    "session_key": "9mzdWWKQ5HJWV8YU9a6K/zT8y2jWbYwBjwHV9QidxSCqmVyeTViytt/RMzJ1/7gjmyHVYr81jXXZeNXYdA6KGkF+3G4BMA==",
    "scope": "public brain_all_scope audio_voice_assistant_get audio_tts_post wise_adapt lebo_resource_base lightservice_public hetu_basic lightcms_map_poi kaidian_kaidian ApsMisTest_Test权限 vis-classify_flower bnstest_fasf lpq_开放",
    "refresh_token": "25.f4ee85540ae20e0591878a71b375e6c6.315360000.1829219144.282335-10567712",
    "session_secret": "c8170d94d279694d4f844b01ef6bbe09",
    "expires_in": 2592000
}

acess_token =  24.6ed051e0ba2b1fe944da549846a4b39d.2592000.1499854092.282335-9750820
'''
class YuYin(object):
    """docstring for yuyin."""
    def __init__(self):

        return None

    def yuyin(self,text):

        url  = "http://tsn.baidu.com/text2audio?tex=%s&lan=zh&per=0&cuid=98:01:a7:b0:90:23&ctp=1&tok=24.915d8775f6fba335f4c3f3bd4e844c3f.2592000.1578649575.282335-18001660"
        text = urllib.quote(text)
        url  = url % text

        webbrowser.open(url)
        return url

if __name__ == '__main__':
    text = "大撒的见风使舵了房间"
    re   = YuYin().yuyin(text)
