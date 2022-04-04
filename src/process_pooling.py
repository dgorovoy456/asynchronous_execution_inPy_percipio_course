import os
from multiprocessing import Pool

num_list = [1, 2, 3, 4, 5]


def cal_square(n):
    return n * n


result = []

for num in num_list:
    result.append(cal_square(num))

print(result)

print(os.cpu_count())

print('################################################')

print(os.cpu_count())


def cal_square(n):
    print(n, os.getgid())
    return n * n


result = []

for num in num_list:
    result.append(cal_square(num))

print(result)

print('#################################################')


p = Pool(5)

pool_result = p.map(cal_square, num_list)

p.close()

print(pool_result)
