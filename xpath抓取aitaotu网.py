import urllib.request
from lxml import etree
import re
import random
import os


class Spider:
    def __init__(self):
        ''''''
    def open_url(self,url):
        '''打开页面'''
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3427.400 QQBrowser/9.6.12513.400'}

        request = urllib.request.Request(url,headers = headers)
        html = urllib.request.urlopen(request).read().decode('utf-8')
        return html




    def new_link(self,html):
        '''爬取页面中子页面的链接'''
        #解析页面为lxml
        content = etree.HTML(html)
        #通过xpath来爬取子页面的链接，如/guonei/25845.html
        link_list = content.xpath('//div[@id="mainbody"]/ul/li/a[@class="Pli-litpic"]/@href')


        new_links =[]
        for link in link_list:
            #抓取到子页面链接后，重新组合成新的可打开的网页链接
            link ='https://www.aitaotu.com'+link
            new_links.append(link)
        for new_link in  new_links:
            #重新组合后的链接，再次打开，爬取翻页链接
            spider.page_url(new_link)

    def open_img(self,img_url):
        '''爬取每一页的大图链接和图片名称，并组合成一个字典组合'''
        #传入每一页链接，并打开页面
        img_html = spider.open_url(img_url)
        content = etree.HTML(img_html)
        #抓取图片标题,做文件夹名使用
        '''title = content.xpath('//div[@class="photo"]//div/h1/text()')
        if not os.path.exists('d:/imgs/%s'%(title[0])):
            os.mkdir('d:/imgs/%s'%(title[0]))'''
        #抓取的大图链接列表
        img_list = content.xpath('//div[@class="big-pic"]/div/p//img/@src')
        #抓取的图片名称
        img_name =content.xpath('//div[@class="big-pic"]/div/p//img/@alt')
        #组合成一个字典
        file =dict(zip(img_list,img_name))
        #保存下载图片
        for key in file:
            print('正在下载'+file[key])
            urllib.request.urlretrieve(key, 'd:/imgs/%s.jpg' % (file[key]))







    def page_url(self,new_link):
        '''获取末页链接，找到所有翻页的链接'''
        #new_link为子页面网页链接
        img_html = spider.open_url(new_link)
        content = etree.HTML(img_html)
        #爬取末页链接，如/meinv/34574_12.html
        end_page = content.xpath('//div[@class="pages"]/ul/li/a[text()="末页"]/@href')

        #通过正则表达式来选出页码和网页地址
        pattern = re.compile('(.*?)_(.*?).html')
        a = pattern.match(end_page[0])
        #12
        page_num =a.group(2)
        #/meinv/34574
        url = a.group(1)
        page_urls =[]
        for i in range(1,int(page_num)+1):
            #组合子页面中下一页的所有链接
            page_url ='https://www.aitaotu.com'+url +'_'+str(i)+'.html'
            page_urls.append(page_url)
        for img in page_urls:

            #传入每一页链接，爬取大图链接

            spider.open_img(img)




if __name__ =='__main__':
    page = input('请输入要爬取的页码：')
    url ='https://www.aitaotu.com/tag/aiss/'+page+'.html'
    spider = Spider()
    html = spider.open_url(url)
    new_links =spider.new_link(html)






