 #!/usr/bin/env python
# coding:utf8

import sys
reload(sys)
sys.setdefaultencoding("utf8")

# 加载库
import urllib
import urllib2
import json
from bs4 import BeautifulSoup
import datetime
import os
import requests

def getTemplate():
   return '''---
title:  English exercise
date:   <title>
categories: 英语早操
thumbnail: http://p1.bpimg.com/567571/7720b01fba7e27d6.png
tags: English
photos:
- <picture>
---

"<content1>"
<p><content2></p>
'''
def getcontent(today):
    # today=str(datetime.datetime.now().strftime('%Y-%m-%d'))
    url = 'https://rest.shanbay.com/api/v2/quote/quotes/today/'
    response = json.loads(requests.request(url=url,method="get").text)
    # html = BeautifulSoup(response,"html.parser")

    try:
        content = response['data']["content"]
        translation = response["data"]["translation"]
        # content= html.find_all('div',attrs={"class": "content"})[0]
        # content = content.get_text()
    except:
        pass

    return content,translation



def convert_date_to_num():
	a = datetime.datetime.now()
	b =str(a)
	date = datetime.datetime.strptime("2017-01-20", "%Y-%m-%d")
	delta =  (a-date).days
	return b,delta

if __name__ == '__main__':
     today=str(datetime.datetime.now().strftime('%Y-%m-%d'))
     print (getcontent(today))   

'''
    files = getTemplate()
	content = getcontent()[0]
	translation = getcontent()[1]
	date = str(datetime.datetime.now().strftime('%Y-%m-%d'))
	delta = str(convert_date_to_num()[1])

	files = files.replace("<title>",date)
	files = files.replace("<content1>",content)
	files = files.replace("<content2>",translation)

	w = open(date +"-English-exercise-"+ delta +'day.md','w')
	w.write(files)
	w.close()
	print "create new post"



	# terminal = "mv "+ date +"-English-exercise-"+ delta +"day.md ../hexo_test/source/_posts"
	# os.system(terminal)


	mv = "cd ../hexo_test"
	generate = "hexo generate"
	deploy = "hexo deploy"
	try:
		os.system(mv)
	except:
		print "mv error"
		exit()

	try:
		os.system(generate)
	except:
		print "hexo generate error"
		exit()

	try:
		os.system(deploy)
		print "well done!"
	except:
		print "hexo deploy error"
		exit()'''
