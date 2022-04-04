import time
from multiprocessing import Pool


def sum_square(numbers):
    s = 0
    for i in range(numbers):
        s += i * i
    return s


def sum_square_with_mp(numbers):
    start_time = time.time()
    p = Pool()
    result = p.map(sum_square, numbers)

    p.close()
    p.join()

    total_time = time.time() - start_time

    print('Processing %d numbers took %.2f seconds using'
          ' multiprocessing' % (len(numbers), total_time))


def sum_square_without_mp(numbers):
    start_time = time.time()
    result = []

    for i in numbers:
        result.append(sum_square(i))

    total_time = time.time() - start_time

    print('Processing %d numbers took %.2f seconds with serial processing'
          % (len(numbers), total_time))


numbers = range(1000)
sum_square_with_mp(numbers)
sum_square_without_mp(numbers)

print('###')

numbers = range(10000)
sum_square_with_mp(numbers)
sum_square_without_mp(numbers)
