#!/usr/bin/eny python
# coding=utf-8


from urllib import request
from os import system
import time as sys_time

my_pid='123'
my_email='xxxx@xxx.com'

try:
    flag=0
    while True:
        url='https://billing.spartanhost.net/cart.php?a=add&pid='+my_pid
        header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
        req=request.Request(url,headers=header)
        page=request.urlopen(req).read()
        with open('content.txt','w') as f:
            f.write('有货了，链接是:'+url)
        if str(page).find('out of stock')>0:
            flag=0
            print('无货')
        else:
            flag=flag+1
            print('有货')
            if flag<3:
                system("mail -s '有货了' {0} < content.txt".format(my_email))
        sys_time.sleep(600)    

except:
    print('脚本异常,退出')

