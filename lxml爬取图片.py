from lxml import etree
import urllib.request


def open_url():
    '''解析url地址
    '''
    #('正在下载' + filename)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3427.400 QQBrowser/9.6.12513.400'}

    url = 'https://www.aitaotu.com/meinv/34574.html'
    req = urllib.request.Request(url, headers=headers)

    html = urllib.request.urlopen(req).read()
    content = etree.HTML(html)
    #print(type(content))
    #result = etree.tostring(content)
    #print(result.decode('utf-8'))
    link_list = content.xpath('//div[@class="pages"]/ul/li/a[text()="末页"]/@href')
    print(link_list[0][-7:-5])

open_url()