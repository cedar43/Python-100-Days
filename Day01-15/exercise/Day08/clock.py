'''
利用类来描述数字时钟，静态特征有时、分、秒；
动态特征有以秒为单位的走时间，显示时间。

Version: 0.1
Author: Cedar43
Date: 2019-12-07
'''

from time import sleep


class clock(object):
    '''clock'''
    def __init__(self, hour=0, minute=0, second=0):
        '''
        :param hour: 时
        :param minute: 分
        :param second: 秒
        '''
        self.hour = hour
        self.minute = minute
        self.second = second

    def run(self):
        self.second += 1
        if self.second == 60:
            self.minute += 1
            self.second = 0
            if self.minute == 60:
                self.hour += 1
                self.minute = 0
                if self.hour == 24:
                    self.hour = 0

    # Flat is better? 但这样每次都要判断*3?
    def run_2(self):
        self.second += 1
        self.minute += self.second // 60
        self.hour += self.minute // 60
        self.second = [0, self.second][self.second < 60]
        self.minute = [0, self.minute][self.minute < 60]
        self.hour = [0, self.hour][self.hour < 24]

    def display(self):
        return '%02d:%02d:%02d' % \
            (self.hour, self.minute, self.second)


def main():
    Clock = clock(23, 59, 50)
    while True:
        print(Clock.display())
        sleep(1)
        Clock.run_2()


if __name__ == '__main__':
    main()
