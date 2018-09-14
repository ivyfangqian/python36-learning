# 作业：
# 1.某市的出租车计费标准为：3公里以内13元，3公里以后每0.5公里加收1元；每等待2.
#   5分钟加收1元；超过15公里的加收原价的50%为空驶费。
#  要求编写程序，对于任意给定的里程数（单位：公里）和等待时间（单位：秒）计算出应付车费

money = 0.0
km = 3.5
wait_time = 180

if 0 < km <= 3:
    money = 13.0
elif 3 < km <= 15:
    money = 13.0 + (km - 3) // 0.5
elif km > 15:
    money = (13.0 + (km - 3) // 0.5) * 1.5
else:
    print("对不起，公里数不能为0或负数")

if wait_time >= 0:
    money += wait_time // 150
else:
    print("对不起，等待时间不能为0或负数")
print("公里数为%.2f公里,等待时间为%ds,应付车费为%.2f元" % (km, wait_time, money))

# 2.一个数如果恰好等于它的因子之和，这个数就称为“完数”。例如6=1＋2＋3.编程找出1000以内的所有完数
for i in range(1, 1000):
    items = [1]
    for j in range(2, i):
        if i % j == 0:
            items.append(j)
    if sum(items) == i:
        print(i, "是完数")

# *3.用python实现选择排序
# 			算法如下：
#                 [49, 38, 27, 45, 13]
# 			第一趟[13, 38, 27, 45, 49]
# 			第二趟[13, 27, 38, 45, 49]
# 			第三趟[13, 27, 38, 45, 49]
# 			第四趟[13, 27, 38, 45, 49]

# n个数
# 第一趟： 1,2,3,n-1
# 第二趟:  2,3,...,n-1
# ...
# 第n-2趟: n-2,n-1
# 第n-1趟: n-1
# 0 - -- n - 1
nums = [49, 38, 27, 45, 13]
n = len(nums)
for i in range(0, n - 1):
    # 找出i+1到n-1的最小值
    smallest_index = i + 1
    for j in range(i + 1, n):
        if nums[j] < nums[smallest_index]:
            smallest_index = j
    # 与nums[i]比较，最小值比nums[i]小，交换
    if nums[smallest_index] < nums[i]:
        nums[smallest_index], nums[i] = nums[i], nums[smallest_index]
print(nums)

nums = [49, 38, 27, 45, 13]
n = len(nums)
for i in range(0, n - 1):
    smallest_index = i + 1
    for j in range(i + 1, n):
        if nums[j] < nums[smallest_index]:
            smallest_index = j
    if nums[i] > nums[smallest_index]:
        nums[i], nums[smallest_index] = nums[smallest_index], nums[i]

print(nums)

# 作业：4.某电信公司的市内通话费计算标准如下：三分钟内0.2元，
# 			  三分钟后每增加一分钟增加0.1元，不足一分钟的按一分
# 			  钟计算。要求编写程序，给定一个通话时间（单位：秒）
# 			  计算出应收费金额。

talk_time = 190
talk_charge = 0.0

if 0 < talk_time <= 180:
    talk_charge = 0.2
elif talk_time > 180 and talk_time % 60 == 0:
    talk_charge = 0.2 + (talk_time - 180) // 60 * 0.1
elif talk_time > 180 and talk_time % 60 != 0:
    talk_charge = 0.2 + (talk_time - 180) // 60 * 0.1 + 0.1
else:
    print("对不起，通话时间不能为0或负数")

print("通话费为%.2f" % talk_charge)

# 5.员工工资表，查询结果集如下：
# ((1, 'zhangsan', 3000), (2, 'lisi', 2500), (3, 'tiantian', 20000))
# 	  1.计算员工的平均工资
# 	 *2.输出工资最高的员工姓名
users = ((1, 'zhangsan', 3000), (2, 'lisi', 2500), (3, 'tiantian', 20000))
summary = 0
for user in users:
    summary += user[-1]
avg_salary = summary / len(users)
print(avg_salary)

max_user = users[0]
for user in users:
    if user[-1] > max_user[-1]:
        max_user = user
print("工资最高的员工为%s,他的工资为%d" % (max_user[1], max_user[-1]))
