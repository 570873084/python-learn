from mysql封装 import MysqlHelp
from hashlib import sha1

#接收用户输入
user = input('请输入用户名：')
pwd = input('请输入密码：')

#加密密码
s1 = sha1()
s1.update(bytes(pwd,encoding='utf-8'))
pw2 = s1.hexdigest()
print(pw2)

query = 'select passwd from user where name =%s'
mysql = MysqlHelp(host='localhost',user='root',password='33655869',database='user',port=3306)

result= mysql.query_all(query,args=[user])
if len(result) == 0:
    print('用户名错误')
elif result[0][0] == pw2:
    print('登陆成功')