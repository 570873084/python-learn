import urllib.request
import re




class SpiderPage:
    def __init__(self):
        self.page = 20
        self.switch = True

    def load_page(self):
        '''内涵段子内涵爬取

                  '''
        url ='http://www.neihan8.com/article/index_'+ str(self.page)+'.html'
        headers ={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3427.400 QQBrowser/9.6.12513.400'}
        request = urllib.request.Request(url,headers=headers)
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf = 8')
        #print(html)
        #正则匹配规则
        pattern = re.compile('<div\sclass="desc">(.*?)</div>',re.S)
        content = pattern.findall(html)
        print('正在下载数据...')
        self.deal_page(content)

    def deal_page(self,content):
         '''处理爬取的内涵段子'''
         for text in content:
             text = text.replace('&amp;hellip;','').replace('&amp;lsquo;','')
             print(text)
             self.write_page(text)


    def write_page(self,text):
        """把内涵段子写入文件"""
        with open('neihan.txt','a') as f:
            print('正在写入数据...')
            f.write(text)


    def control_page(self):
        '''用户控制'''

        while self.switch:
            control = input('继续运行请按回车键，退出输入：quit')
            if control == 'quit':
                self.switch = False

            self.load_page()
            self.page += 1



if __name__ == '__main__':
    spider = SpiderPage()
    spider.control_page()
