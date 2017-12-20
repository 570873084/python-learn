# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 12:59:18 2017

@author: Administrator
"""

import urllib.request

key = input('请输入需要翻译的词：')
headers ={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3427.400 QQBrowser/9.6.12513.400'}
#post请求通过fiddler抓取url地址
url ='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
#找到webform中的data数据
formdata={'i':key,'from':'AUTO','to':'AUTO','smartresult':'dict','client':'fanyideskwe','salt':'1513315527940','sign':'ba8462e6cc17e2179a510b1884ea44f7','doctype':'json','version':'2.1','keyfrom':'fanyi.web','action':'FY_BY_REALTIME','typoResult':'false'}
#解析data数据
data = urllib.parse.urlencode(formdata).encode('UTF8')
request = urllib.request.Request(url,data =data,headers = headers)
response =urllib.request.urlopen(request)
print(response.read().decode('UTF8'))