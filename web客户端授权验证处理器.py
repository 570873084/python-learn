 import urllib.request

 username = '123'
 password = '123456'
 webserver = '192.168.1.1'
 #构建一个密码管理对象，用于保存和http请求相关的授权账户信息
 passwordMgr =urllib.request.HTTPPasswordMgrWithDefaultRealm()
 #添加授权账户信息，第一个realm域如果没有就写None，后三个依次为站点IP，账户名，密码
 passwordMgr.add_password(None,webserver,username,password)

 httpautu_handler = urllib.request.HTTPBasicAuthHandler(passwordMgr)

 opener = urllib.request.build_opener(httpautu_handler)

 request = urllib.request.Request('http://'+webserver)

 responnse = opener.open(request)

 print(responnse.read())