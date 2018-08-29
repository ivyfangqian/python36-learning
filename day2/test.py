# 4.一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同
number = "12321"
for i in range(len(number) // 2):
    if number[i] != number[-i - 1]:
        print("不是回文数")
        break
else:
    print("是回文数")

# 方法二：
if number == number[::-1]:
    print("是回文数")
else:
    print("不是回文数")

number = 12321
num = number
reverse_num = 0
while number != 0:
    reverse_num = reverse_num * 10 + number % 10
    number //= 10

if num == reverse_num:
    print("是回文数")
else:
    print("不是回文数")
