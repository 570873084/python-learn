# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 10:50:34 2017

@author: Administrator
"""

import urllib.request
import ssl
#json库，对应lxml
import json
#json解析语法，对应xpath
import jsonpath

#解决ssl证书问题urlopen error SSL: CERTIFICATE_VERIFY_FAILED]
context = ssl._create_unverified_context()
#https安全认证，可以用http
#url为json网页
url ='https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%83%AD%E9%97%A8'
headers ={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3427.400 QQBrowser/9.6.12513.400'}
formdata ={'page_limit':'100','page_start':'1'}
#formdata需要编码，解决POST data should be bytes
data = urllib.parse.urlencode(formdata).encode(encoding='UTF8')
print(data)
#传入data数据
request = urllib.request.Request(url,data=data,headers=headers)
print(request)
a=urllib.request.urlopen(request,context = context)
#取出json文件的内容，返回格式为字符串，重新解码成中文
html  =a.read().decode(encoding='UTF8')
#把json格式的字符串，转换为python形式的Unicode格式字符串
unicodestr = json.loads(html)
#用jsonpath筛选电影名,python形式
title =jsonpath.jsonpath(unicodestr,'$..title')
#将python形式的字符串转换成json格式,ensure_ascii默认为true转成ascii，false为unicode
#默认转换中文为ascii，所以需要禁用ascii
array = json.dumps(title,ensure_ascii=False)
with open ('douban.json','w') as f:
    f.write(array)

