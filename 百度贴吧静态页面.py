# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 14:11:38 2017

@author: Administrator
"""

import urllib.request

def open_url(url,filename):
    '''解析url地址
    '''
    print('正在下载'+filename)
    headers ={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3427.400 QQBrowser/9.6.12513.400'}

    req =urllib.request.Request(url,headers = headers)
    
    respones =urllib.request.urlopen(req)
    return (respones.read())
    




def save_url(html,filename):
    '''
    '''
    print('正在保存'+filename)
    with open(filename,'wb') as f:
        f.write(html)
        
    print('*'*30)
    
    
    
    
def run_url(url,start_page,end_page):
    '''爬虫调度器
    '''
    for i in range(start_page,end_page+1):
        pn = str((i-1)*50)
        filename = '第'+str(i)+'页'
        fullurl =url+'&pn='+pn
        html =open_url(fullurl,filename)
        save_url(html,filename)
        
        
        
    
    
    
if __name__ == "__main__":
    url ='https://tieba.baidu.com/f?'
    kw1 = input('请输入需要查询的贴吧：')
    start_page = int(input ('请输入起始页：'))
    end_page=int(input ('请输入结束页：'))
    key = urllib.parse.urlencode({'kw':kw})
    url1 =url+key
    run_url(url1,start_page,end_page)
        