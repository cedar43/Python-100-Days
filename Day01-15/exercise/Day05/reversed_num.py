"""
正整数的反转

Version: 0.1
Author: Cedar43
Date: 2019-12-04
"""

num = int(input('Please input a integrated number：'))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10

print('The reversed number is: %d' % reversed_num)
