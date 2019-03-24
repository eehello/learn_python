#!/usr/bin/eny python
# coding=utf-8


from urllib import request
from os import system
import time as sys_time
import datetime


my_pid='123'
my_email='xxxx@xxx.com'

try:
    flag=0
    while True:

        now_date = datetime.datetime.now()
        end_year = int(now_date.strftime('%Y'))
        end_month = int(now_date.strftime('%m'))
        end_day = int(now_date.strftime('%d'))
        end_hour = int(now_date.strftime('%H'))
        end_minute = int(now_date.strftime('%M'))

        end_times = datetime.datetime(end_year, end_month, end_day, end_hour, end_minute)
        end_time = end_times.strftime('%Y-%m-%d %H:%M')


        url='https://billing.spartanhost.net/cart.php?a=add&pid='+my_pid
        header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
        req=request.Request(url,headers=header)
        page=request.urlopen(req).read()
        with open('content.txt','w') as f:
            f.write(end_time+'有货了，链接是:'+url)
        if str(page).find('out of stock')>0:
            flag=0
            print('无货--'+end_time)
        else:
            flag=flag+1
            print('有货--'+end_time)
            if flag<3:
                system("mail -s '有货了' {0} < content.txt".format(my_email))
        sys_time.sleep(600)    

except:
    print('脚本异常,退出')

