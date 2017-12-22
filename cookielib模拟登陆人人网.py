
import urllib.request
import urllib.parse

import http.cookiejar
#通过cookiejar（）类来构建一个cookiejar对象，用来保存cookie的值
cookie = http.cookiejar.CookieJar()
#通过httpcoolieprocessor构建一个cookie处理器对象，处理cookie
#参数就是构造的cookiejar（）对象
cookie_handler = urllib.request.HTTPCookieProcessor(cookie)
#构建一个自定义opener处理器
opener = urllib.request.build_opener(cookie_handler)
#通过opener.addheaders添加浏览器抱头
headers = ('User-agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36')
opener.addheaders = [headers]
#人人网老的登陆接口
url = 'http://www.renren.com/PLogin.do'

data = {'email':'18857665584','password':'33655869'}
#解码data
data = urllib.parse.urlencode(data).encode()
#第一次是post请求，发送登陆需要的参数，获取cookie
request  = urllib.request.Request(url,data = data)
#发送第一次post请求，生成登陆后的cookie（需要登陆成功）
response = opener.open(request)
#print(response.read().decode('utf-8')
#此次为get请求，这个请求将之前保存下来的cookie一并发送到web服务器，服务器会验证cookie通过
response_ziliao = opener.open('http://www.renren.com/896519956/profile?v=info_timeline')
print(response_ziliao.read().decode())

