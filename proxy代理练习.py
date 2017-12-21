# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 11:00:00 2017

@author: Administrator
"""

import  urllib.request
#代理开关，表示代理是否开关
proxyswitch = True
#构建一个handler代理对象，参数为字典类型，key值为代理类型，value值为代理IP：端口号
#代理地址在www.xicidaili.com上找的，很多代理IP不能用，私密代理格式为{"http" : "user：passwd@IP：端口号"}
httpproxy = urllib.request.ProxyHandler({'http':'112.114.98.44:8118'})
#构建一个无代理handler
nullproxy = urllib.request.ProxyHandler({})

if proxyswitch:
    opener = urllib.request.build_opener(httpproxy)
else:
    opener = urllib.request.build_opener(nullproxy)
#构建一个全局opener。之后的所有请求都可以用URLopen()方式打开，也附带handle功能 
#如果只需要请求一次，就没必要构建全局opener
urllib.request.install_opener(opener)
#百度可以不用构建headers
request = urllib.request.Request('http://www.baidu.com/')

response = urllib.request.urlopen(request)

print(response.read().decode('utf-8'))
'''请求一次，打开方式
r = opener.open('http://www.sougou.com/')
print(r.read().decode('utf-8'))

'''
