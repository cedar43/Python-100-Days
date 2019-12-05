"""
Fibonacci sequence

Version: 0.1
Author: Cedar43
Date: 2019-12-05
"""
# import time
# Method 1
# strat_1 = time.process_time_ns()
num = int(input('请输入需要求的FS数个数：'))
f = list(range(num))
f[0] = 1
f[1] = 1
for i in range(2, num):
    f[i] = f[i-1] + f[i-2]
print(f)
# print(time.process_time_ns() - strat_1)

# Method 2
# start_2 = time.process_time_ns()
fs = [1, 1]
x, y = 1, 1
for i in range(2, num):
    z = x + y
    fs.append(z)
    x, y = y, z
print(fs)
# print(time.process_time_ns() - start_2)
