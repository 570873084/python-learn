# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 10:50:34 2017

@author: Administrator
"""

import urllib.request
import ssl

#解决ssl证书问题urlopen error SSL: CERTIFICATE_VERIFY_FAILED]
context = ssl._create_unverified_context()
#https安全认证，可以用http
url ='https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%83%AD%E9%97%A8'
headers ={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3427.400 QQBrowser/9.6.12513.400'}
formdata ={'page_limit':'50','page_start':'1'}
#formdata需要编码，解决POST data should be bytes
data = urllib.parse.urlencode(formdata).encode(encoding='UTF8')
print(data)
#传入data数据
request = urllib.request.Request(url,data=data,headers=headers)
print(request)
a=urllib.request.urlopen(request,context = context)
#重新解码成中文
print(a.read().decode(encoding='UTF8'))

