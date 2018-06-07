import pandas as pd
import numpy as np
import tushare as ts
import time
import threading
import matplotlib.pyplot as plt

class get_stock(object):
    def __init__(self):
        #初始化
        self.sto_df = pd.DataFrame(columns=['price'])

    def stock(self,id1,id2):

        global timer,a
        #从tushare获取实时股票行情
        ts.
        df1 =ts.get_realtime_quotes(id1)
        df2 =ts.get_realtime_quotes(id2)
        p =df1[['name','price','volume','date','time']]
        p2 = df2[['name', 'price', 'volume', 'date', 'time']]
        #如果两只股票时间相同，保存数据
        if str(p['time']) == str(p2['time']):
            #print((str(p['time']))[5:14])
            #索引为时间
            self.sto_df.loc[((str(p['time']))[5:14]).replace('\n','')] =float(p['price'])-float(p2['price'])
            #重新设置索引
            b = self.sto_df.reset_index()
            #print(b)
            #将index列属性改为时间
            b['index'] = pd.to_datetime(b['index'])

            print(b)
            #fig = plt.figure(figsize =(3,3))
            plt.plot(b['index'],b['price'],bins=20)
            plt.xticks(rotation = 45)
            plt.show()


        timer = threading.Timer(3, a.stock,[id1,id2])     #Timer只能传函数，例stock，不能是stock（），函数的参数则要放到外面
        timer.start()
            #print(type(p))
            #print(p)
        #print(type(str(p2['time'])))



if __name__ =='__main__':
    id1 = input('请输入股票代码:')
    id2 = input('请输入股票代码:')
    #实例化类
    a =get_stock()
    #设置每3秒执行程序
    timer = threading.Timer(3,a.stock,[id1,id2])
    timer.start()

