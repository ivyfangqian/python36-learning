# -------------------datetime模块-----------------
# 官方文档：https://docs.python.org/3/library/datetime.html
# datetime模块是python内置的强大时间处理模块，datetime定义了以下几种类
# datetime.date：表示日期的类。常用的属性有year, month, day；
# datetime.time：表示时间的类。常用的属性有hour, minute, second, microsecond；
# datetime.datetime：表示日期时间。
# datetime.timedelta：表示时间间隔，即两个时间点之间的长度。
# datetime.tzinfo：与时区有关的相关信息

import datetime, time

# datetime.date(year, month, day),所有参数必传，得到指定的datetime.date对象
print(datetime.date(2018, 8, 23))
# 获取当天的datetime.date对象
print(datetime.date.today())
# datetime.date.fromtimestamp(time_stamp)根据时间戳获取datetime.date对象
time_stamp = time.time()
cur_date = datetime.date.fromtimestamp(time_stamp)
print(cur_date)
# 获取日期的年、月、日
print(cur_date.year)
print(cur_date.month)
print(cur_date.day)
# isoweekday()获取日期对应是星期几
print(cur_date.isoweekday())
# isformat()获取日期对应格式化字符串，格式为YYYY-MM-DD
print(cur_date.isoformat())
# strftime(fmt),根据自定义的格式化字符串，对日期进行格式化
print(cur_date.strftime("%Y~%m~%d"))

# datetime.time(hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0),全部为非必填参数
# microsecond为微秒，一微秒为百万分之一秒
print(datetime.time)

# 得到指定的datetime.time对象
t = datetime.time(11, 30, 20, 188)
print(t)
# 获取datetime.time对象的时、分、秒、微秒
print(t.hour)
print(t.minute)
print(t.second)
print(t.microsecond)
# 得到datetime.time对象的字符串，格式为HH:MM:SS
print(t.isoformat())
# 根据指定格式化字符串，得到datetime.time对象的字符串表示
print(t.strftime('%H:%M:%S'))

print(datetime.datetime)
print(datetime.datetime(2018,8,23))