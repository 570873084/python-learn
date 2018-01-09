import requests
from bs4 import BeautifulSoup


#构建一个session对象，用于保存页面cookie
sess =requests.Session()
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3427.400 QQBrowser/9.6.12513.400'}
url = 'https://www.zhihu.com/signup?next=%2F'
#首先打开页面，看是否有获取需要post的数据
html = sess.get(url,headers=headers).text
#lxml解析
bs = BeautifulSoup(html,'lxml')
#beautifulsoup用法
_xsrf = bs.find("button",attrs={"type":"button"}).get('class')
#需要post的数据
data={'':''
}
#post地址
url =''
#传入post数据，保存cookie在sess里面
response =sess.post(url,data=data,headers =headers)
#sess里面已经保存cookie，这样就可以访问主页了
rep =sess.get(url,headers =headers)

