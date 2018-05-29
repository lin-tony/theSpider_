import re
import requests
from bs4 import BeautifulSoup

loginurl = 'http://jwxt.gdufe.edu.cn/jsxsd/xk/LoginToXkLdap'  # 实际提交表单页面
headers = {
    "Accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Host': 'jwxt.gdufe.edu.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}  # UA 使得服务器能够识别客户使用的操作系统及版本、CPU 类型、浏览器及版本、浏览器渲染引擎、浏览器语言、浏览器插件等
geturl = 'http://jwxt.gdufe.edu.cn/jsxsd/xskb/xskb_list.do'  # 需要爬取的登录之后的页面
datas = {'USERNAME': '16251104218', 'PASSWORD': 'zitong233'}

s = requests.session()
Post = s.post(loginurl, data=datas, headers=headers)
Get = s.get(geturl, cookies=Post.cookies, headers=headers)
Soup = BeautifulSoup(Get.content, 'html5lib')
zz1 = '\[.*?]'
zz2 = '(?:\d+\,)|(?:\d+\(周\))'
zz3 = '(?:[0-9]|\,|-)+\((?:单|双)*周\)'
#
list1 = Soup.findAll('div', attrs={"class":"kbcontent1"})

f = open("C:/Users/tony/Desktop/5.txt", "w", encoding='utf-8')

for i in list1:
    if(i.text==" "):#空则跳过
        continue
    f.write("周"+str(i.get('id'))[-3:-2]+"\n")
    f.write(str(re.findall(zz3, str(i.text))[0]))
    f.write(str(re.findall(zz1, str(i.text))[-1])+"\n")
    f.write(i.text+'\n\n')

    print(str(re.findall(zz3, str(i.text))[0]))#周数
    #print(re.findall(zz2, str(i.text)))
    print(re.findall(zz1, str(i.text))[-1])#节数
    print("!"+i.text+'\n')



