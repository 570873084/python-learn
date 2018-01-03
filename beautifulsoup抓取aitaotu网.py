# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 11:03:43 2017

@author: Administrator
"""

import requests
import re
import urllib.request
import os
from bs4 import BeautifulSoup
import random

def open_url(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3427.400 QQBrowser/9.6.12201.400')
    respone = urllib.request.urlopen(req)
    return (respone.read())


#分页地址
def fenye(url):
    html = open_url(url)
    soup = BeautifulSoup(html,'lxml')
    a = soup.find_all('h2')
#print(type(a))
#print(a)
    c=[]
    for i in a:
        c.append(i.find('a')['href'])
    return(c)

#下一页地址
def next_url(url):
    html = open_url(url)
    soup = BeautifulSoup(html,'lxml')
    #print(soup)
    a = soup.find('a',text=re.compile('下一页'))
#print(a.string)
    return (a['href'])


#文件夹名字以标题    
def title(url):
    html = open_url(url)
    soup = BeautifulSoup(html,'lxml')
#print(soup)
    a = soup.find('h1')
    return(a.string)
 

#当前页面图片地址
def addr_url(url):
    
    html = open_url(url)
    soup = BeautifulSoup(html,'lxml')
    #print(soup)
    a = soup.find_all('p')
   
    img_addrs =[]
    for i in a:
        c=i.find_all('img')
        for m in c:
            img_addrs.append(m['src'])
    return(img_addrs)


#创建文件夹
def wenjianjia():
    a = title(url)
    os.mkdir(a)  
    # 将脚本的工作环境移动到创建的文件夹下  
    os.chdir(a)

#保存图片
def save_img(img_addrs):
    a =title(url)
    count = random.randint(1,20000)
    for photo in img_addrs:
        
        print(photo)
        urllib.request.urlretrieve(photo,'d:/imgs/a/%d-%s.jpg'%(a,count))
        count += 1
        

url = 'http://www.bfpgf.com/page/1?s=aiss'
one =fenye(url)
for two in one:
    img_addrs = addr_url(two)
    title(two)
    wenjianjia()
    save_img(img_addrs)



