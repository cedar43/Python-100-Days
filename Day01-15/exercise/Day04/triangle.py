"""
按要求打印三角形图案

Version: 0.1
Author: Cedar43
Data: 2019-12-04
"""

for i in range(1, 6):
    a = i * '*'
    print('%s\n' % a)

for i in range(1, 6):
    a = (5 - i) * ' ' + i * '*'
    print('%s\n' % a)

for i in range(1, 6):
    a = (5 - i) * ' ' + i * '*'\
        + (i - 1) * '*' + (5 - i) * ' '
    print('%s\n' % a)
