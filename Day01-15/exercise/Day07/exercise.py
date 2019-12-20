'''
Little exercise for Day07

Version: 0.1
Author: Cedar43
Date: 2019-12-06
'''

import os
import time
import random
from datetime import datetime


def fun():
    content = '北京欢迎你为你开天辟地......'
    while True:
        os.system('cls')
        print(content)
        time.sleep(0.2)
        content = content[1:] + content[0]


# if __name__ == '__main__':
#     main()


def generate_code(code_len=4):
    """
    生成指定长度的验证码

    :param code_len: 验证码的长度(默认4个字符)

    :return: 由大小写英文字母和数字构成的随机验证码
    """
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyz\
        ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    last_pos = len(all_chars) - 1
    code = ''
    for i in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code


def get_suffix(filename, has_dot=False):
    """
    获取文件名的后缀名

    :param filename: 文件名
    :param has_dot: 返回的后缀名是否需要带点
    :return: 文件的后缀名
    """
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''


def max2(x):
    m1 = max(x)
    x.remove(m1)
    m2 = max(x)
    return m1, m2


def is_leap_year(year):
    """
    判断指定的年份是不是闰年

    :param year: 年份
    :return: 闰年返回True平年返回False
    """
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def which_day(year, month, date):
    """
    计算传入的日期是这一年的第几天

    :param year: 年
    :param month: 月
    :param date: 日
    :return: 第几天
    """
    day_of_month = [[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
                    [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
                    ][is_leap_year(year)]  # 相当于day_of_month[index],判断True取1
    total = 0
    for i in range(month - 1):
        total += day_of_month[i]
    return total + date


def range_from_d2t(year, month, date):
    """
    计算传入的日期距离今天多少天

    :param year: 年
    :param month: 月
    :param date: 日
    :return: 第几天
    """

    today = datetime.today().strftime('%Y-%m-%d')
    # today = list(map(int,today.split('-')))
    today = [int(i) for i in today.split('-')]
    total_year = 0
    if year <= today[0]:
        for i in range(year, today[0]):
            day_of_year = [365, 366][is_leap_year(i)]
            total_year += day_of_year
        total = total_year - which_day(year, month, date)\
            + which_day(today[0], today[1], today[2])
    else:
        for i in range(today[0], year):
            day_of_year = [365, 366][is_leap_year(i)]
            total_year += day_of_year
        total = total_year + which_day(year, month, date)\
            - which_day(today[0], today[1], today[2])
    return total if total >= 0 else -total


def yhtriangle():
    num = int(input('Number of rows: '))
    yh = [[]] * num
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end='\t')
        print()
