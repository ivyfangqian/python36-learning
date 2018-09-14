# # 作业：4.某电信公司的市内通话费计算标准如下：三分钟内0.2元，
# # 			  三分钟后每增加一分钟增加0.1元，不足一分钟的按一分
# # 			  钟计算。要求编写程序，给定一个通话时间（单位：秒）
# # 			  计算出应收费金额。
#
# talk_time = input("请输入通话时长:")
# talk_charge = 0.0
#
# if talk_time.isdigit():
#     talk_time = int(talk_time)
#     if 0 < talk_time <= 180:
#         talk_charge = 0.2
#         print("通话时长%d,通话费用%.2f" % (talk_time, talk_charge))
#     elif talk_time > 180 and talk_time % 60 == 0:
#         talk_charge = 0.2 + (talk_time - 180) // 60 * 0.1
#         print("通话时长%d,通话费用%.2f" % (talk_time, talk_charge))
#     elif talk_time > 180 and talk_time % 60 != 0:
#         talk_charge = 0.2 + (talk_time - 180) // 60 * 0.1 + 0.1
#         print("通话时长%d,通话费用%.2f" % (talk_time, talk_charge))
#     else:
#         print("通话时长不能为0")
#
# else:
#     print("对不起，输入的通话时长格式不合法")

# 作业：
# 1.某市的出租车计费标准为：3公里以内13元，3公里以后每0.5公里加收1元；每等待2.
#   5分钟加收1元；超过15公里的加收原价的50%为空驶费。
#  要求编写程序，对于任意给定的里程数（单位：公里）和等待时间（单位：秒）计算出应付车费
money = 0.0
km = 5.2
wait_time = 180

# int，float判断类型
if isinstance(km, float):
    if 0 < km <= 3:
        money = 13.0
    elif 3 < km <= 15:
        money = 13.0 + (km - 3) // 0.5
    elif km > 15:
        money = (13.0 + (km - 3) // 0.5) * 1.5
    else:
        print("公里数不能小于等于0")
else:
    print("公里数不合法")

if isinstance(wait_time, int):
    if wait_time > 0:
        money += wait_time // 150
    else:
        print("等待时间不能小于等于0")
else:
    print("时间不合法")

print("公里数为%.2f,等待时间为%d,总的车费为%.2f" % (km, wait_time, money))

# 2.一个数如果恰好等于它的因子之和，这个数就称为“完数”。
# 例如6=1＋2＋3.编程找出1000以内的所有完数
# 5 - - 1
# 6 - -1, 2, 3 - - 2, 3, 4, 5
# 8 - - 1, 2, 4 - - 2, 3, 4, 5, 6, 7

# for i in range(1, 1001):
#     summary = 0
#     for j in range(2, i):
#         if i % j == 0:
#             summary += j
#     if summary+1 == i:
#         print(i)


# for i in range(1, 1001):
#     items = [1]
#     for j in range(2, i):
#         if i % j == 0:
#             items.append(j)
#     if sum(items) == i:
#         print(i, items)

# 5.员工工资表，查询结果集如下：
# ((1, 'zhangsan', 3000), (2, 'lisi', 2500), (3, 'tiantian', 20000))
# 	  1.计算员工的平均工资
# 	 *2.输出工资最高的员工姓名
data = ((1, 'zhangsan', 3000), (4, "liulaoshi", 20000), (2, 'lisi', 2500), (3, 'tiantian', 20000))
salary_sum = 0
for user in data:
    salary_sum += user[-1]
print("平均薪资%.2f" % (salary_sum / len(data)))

#
max_user = data[0]
for user in data:
    if user[-1] > max_user[-1]:
        max_user = user
print("最高工资是%d，员工姓名%s" % (max_user[-1], max_user[1]))
