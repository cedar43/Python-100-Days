"""
Perfect number like 28 = 1 + 2 + 4 + 7 + 14

Version: 0.1
Author: Cedar43
Date: 2019-12-05
"""
while True:
    num = int(input("请输入需要寻找的最大正整数："))
    if num <= 0:
        print("请输入一个正整数！")
    else:
        break
pn = []
for i in range(1, num + 1):
    end = int(i / 2)
    factor = []
    for j in range(1, end + 1):
        if i % j == 0:
            factor.append(j)
    if i == sum(factor):
        pn.append(i)
print(pn)
