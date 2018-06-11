#datetime模块的使用　参考https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431937554888869fb52b812243dda6103214cd61d0c2000

#datetime模块下有５个类：datetime time date timezone timedelta
from datetime import datetime

#获取当前系统时间
now=datetime.now()
print(now)

#用参数构造一个datetime
dt=datetime(2019,2,3,12,33,20)
print(dt)

#时间戳：在计算机中，时间实际上是用数字表示的。我们把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，记为0（1970年以前的时间timestamp为负数），当前时间就是相对于epoch time的秒数，称为timestamp。timestamp的值与时区毫无关系，因为timestamp一旦确定，其UTC时间就确定了

#timestamp=0=1970-1-1 00:00:00 UTC+0:00
#timestamp=0=1970-1-1 08:00:00 UTC+8:00

#将datetime转化为timstamp
t=dt.timestamp()
print(t)

#将timestamp转化为datetime,默认转为系统时区
print(datetime.fromtimestamp(t))
print(datetime.utcfromtimestamp(t))

#str转datetime:strptime方法
cday=datetime.strptime('2018-1-1 12:23:34','%Y-%m-%d %H:%M:%S')
print(cday)


#datetime转str:strftime方法
now=datetime.now()
print(now.strftime('%a,%m %d %H:%M')

#时间加减timedelta
from datetime import timedelta
now=datetime.now()
print(now-timedelta(hours=2))


#ｕｔｃ时间转为本地时间
from datetime import timezone
tz_utc_8=timezone(timedelta(hours=8))
now= datetime.now()
dt=now.replace(tzinfo=tz_utc_8)

#时区转化
utc_dt=datetime.uctnow().replace(tzinfo=timezone.utc)
print(utc_dt)
bj_dt=utc_dt.astimezone(timezone(timedelta(hours=8)))




