"""
输入正整数判断是否为素数

Version: 0.1
Author: Cedar43
Data: 2019-12-04
"""
from math import sqrt
num = int(input("请输入一个正整数："))
if num <= 0:
    print("请输入一个正整数！")
end = int(sqrt(num))
is_prime = True
for i in range(2, end + 1):
    if num % i == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('%d是素数' % num)
else:
    print('%d不是素数' % num)
