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

# datetime.time(hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)
print(datetime.time(11, 30, 20, 188))
print(datetime.time)
t = datetime.time(16, 24, 15)
print(t)
print(t.hour)
print(t.minute)
print(t.second)
print(t.isoformat())
print(t.strftime('%H:%M:%S'))
