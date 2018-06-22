import pymysql

class MysqlHelp(object):
    def __init__(self,host,user,password,database,port,charset='utf8'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.charset = charset

    def open(self):
        #链接数据库
        self.conn =pymysql.connect(self.host,self.user,self.password,self.database,self.port,self.charset)
        self.cursor =self.conn.cursor()

    def close(self):
        #关闭数据库
        self.cursor.close()
        self.conn.close()

    def curd(self,query,args):
        #增加修改删除数据库内容
        try:
            self.open()
            self.cursor.execute(query,args)
            self.conn.commit()
            self.close()
        except Exception,e:
            print('woring')


    def query_all(self,query,args=[]):
        #查询数据库所有内容
        try:
            self.open()
            self.cursor.execute(query,args)
            result = self.cursor.fetchall()
            self.close()
            return result
        except Exception,e:
            print('bad')




