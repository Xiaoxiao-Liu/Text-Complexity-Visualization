#encoding:utf-8
import turtle
import time
'''
关于三角形的规则：3边相等的三角形叫等边三角形 =>
等边三角形的三个角也相等 => 等边三角形的内角为60度
所以在本题中，要求用turtle的两个函数，画一个变长为100，内角为60的等边三角形
变长为100用turtle.fd()函数来实现
角度用turtle.seth()来控制
但是turtle.seth的角度是这样的：
如果seth(0),它是往右边直走，
如果参数为正数，它往左边转动，为负数，就往右边转动。
我们如果设置旋转角度为60，它最后是回不来起点的，
所以我们设置旋转角度为180-60。
'''
for i in range(0,3):
    turtle.seth(i * 120)
    turtle.fd(100)
    time.sleep(1)

