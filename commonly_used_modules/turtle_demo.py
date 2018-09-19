__author__ = "ivy"
__time__ = "2018-09-19"

import turtle

turtle.title("正方形螺旋线")
turtle.setup(400, 400, 0, 0)
turtle.speed(10)  # 设置绘制时的速度
turtle.pensize(2)  # 设置画笔尺寸
turtle.color("red")  # 设置画笔颜色

for x in range(100):
    turtle.forward(2 * x)
    turtle.left(90)
