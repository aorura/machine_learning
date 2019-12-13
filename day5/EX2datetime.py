from datetime import datetime
import pandas as pd

now = datetime.now()
print('\n',now,'\n')
print('\n',"{0}년 {1}월 {2}일".format(now.year, now.month,now.day),'\n')

delta = datetime(2018, 1, 7) - datetime(2015, 6, 24, 8, 15)
print('\n', delta, '\n')
print('\n', "days:{0} seconds:{1}".format(delta.days, delta.seconds),'\n')

from datetime import timedelta

start = datetime(2011,1,7)

print('\n',start+timedelta(12),'\n')
print('\n',start-2*timedelta(12),'\n')

stamp = datetime(2017,1,3)
print('\n',str(stamp),'\n')
print('\n',stamp.strftime('%Y-%m-%d'),'\n')

value='2017-01-03'
date1=datatime.strptime(value,'%Y-%m-%d')
print('\n',data1,'\n')

datestrs=['7/6/2018','8/6/2018']
print('\n',[datetime.strptime(x,'%m/%d/%Y') for x in datestrs],'\n')

from dateutil.parser import parse
print('\na',parse('2017-01-03'),'\n')
print('\na',parse('Jan 31, 2001 10:45 PM'), '\n')