import time
from concurrent.futures import ThreadPoolExecutor


def return_after_n_seconds(n, message):
    time.sleep(n)
    return message


pool = ThreadPoolExecutor(3)
submited_job = pool.submit(return_after_n_seconds, 5, 'Hello')

print(submited_job.done())

print(submited_job.result())

print(submited_job.done())

print('################################')

num_list = [2, 3, 4, 5, 6]


def cal_square(x):
    return x * x


def executor_func():
    with ThreadPoolExecutor(max_workers=3) as executor:
        results = executor.map(cal_square, num_list)

    return results


square_data = executor_func()

print(list(square_data))
