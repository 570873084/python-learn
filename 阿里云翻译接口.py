import urllib.request
import ssl
import urllib.parse


key  = input('请输入需要翻译的词：')
context = context = ssl._create_unverified_context()

url ='https://fanyi.market.alicloudapi.com/rest/160601/mt/translate.json'
appcode ='4a079bc226ca47ae8a40b2566bdb6679'
headers ={"Content-Type":"application/x-www-form-urlencoded; charset=utf-8","Authorization":"APPCODE 4a079bc226ca47ae8a40b2566bdb6679"}
formatdata = {"format":"text","q":key,"source":"auto","target":"en"}
data =urllib.parse.urlencode(formatdata).encode('UTF8')
request = urllib.request.Request(url,data=data,headers=headers)
#request.add_header('Authorization', 'APPCODE ' + appcode)
#request.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')

response = urllib.request.urlopen(request,context =context)
print(response.read())