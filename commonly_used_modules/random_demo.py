import random

# random - -生成随机数
# random.uniform(a, b)
# 返回a和b范围内的随机实数[a, b),float类型
rand_num = random.uniform(1, 100)
print(rand_num)

# random.randint(a, b)
# 返回整数a和b范围内整数[a, b]
rand_num = random.randint(1, 100)
print(rand_num)

# random.random()
# 返回随机数，它在0和1范围内(不包括1)
rand_num = random.random()
print(rand_num)

# random.randrange(start, stop[, step])
# 返回整数范围的随机数,step默认为1，如果设定step，那么随机数只会从这些range(start,stop,step)中选取
rand_num = random.randrange(0, 100, 5)
print(rand_num)

# random.sample(array, x)
# 从集合或元祖中返回随机x个元素 - -集合形式
numbers = [1, 3, 5, 4, 6, 8, 9]
rand_nums = random.sample(numbers, 2)
print(rand_nums)


# random.shuffle(array)
# 给指定的序列进行随机移位
random.shuffle(numbers)
print(numbers)
