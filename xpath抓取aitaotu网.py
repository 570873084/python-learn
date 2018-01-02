import urllib.request
from lxml import etree




class Spider:
    def __init__(self):
        self.switch = True
    def open_url(self,url):
        '''打开页面'''
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3427.400 QQBrowser/9.6.12513.400'}

        request = urllib.request.Request(url,headers = headers)
        html = urllib.request.urlopen(request).read().decode('utf-8')
        return html




    def img_url(self,html):
        '''爬取页面中子页面图片的链接'''
        content = etree.HTML(html)
        link_list = content.xpath('//div[@id="mainbody"]/ul/li/a[@class="Pli-litpic"]/@href')
        new_link =[]
        for link in link_list:
            link ='https://www.aitaotu.com'+link
            new_link.append(link)
        return(new_link)

    def open_img(self,img_url):
        '''打开子页面图片链接，爬取其中的大图链接'''

        img_html = spider.open_url(img_url)
        content = etree.HTML(img_html)
        link_list = content.xpath('//div[@class="big-pic"]/div/p//img/@src')
        return(link_list)


    def end_page(self,img_url):
        '''获取末页链接，找到所有翻页的链接'''
        img_html = spider.open_url(img_url)
        content = etree.HTML(img_html)
        link_list = content.xpath('//div[@class="pages"]/ul/li/a[text()="末页"]/@href')
        print(link_list)































if __name__ =='__main__':
    page = input('请输入要爬取的页码：')
    url ='https://www.aitaotu.com/tag/aiss/'+page+'.html'
    spider = Spider()
    html = spider.open_url(url)
    img_urls =spider.img_url(html)
    for img_url in img_urls:
        spider.end_page(img_url)



