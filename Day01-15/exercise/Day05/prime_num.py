"""
输入正整数判断是否为素数

Version: 0.1
Author: Cedar43
Data: 2019-12-04
"""
from math import sqrt
while True:
    num = int(input("请输入一个正整数："))
    if num <= 0:
        print("请输入一个正整数！")
    else:
        break
pn = []
for i in range(2, num + 1):
    end = int(sqrt(i))
    is_prime = True
    for j in range(2, end + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime and i != 1:
        pn.append(i)
print(pn)
