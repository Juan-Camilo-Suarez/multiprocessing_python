from multiprocessing import Pool
from time import sleep

"""
- function apply is used to define task for one of the process 
- for any of the processes
- it's not block the processes and return AsyncResult object.
"""


def add_numbers(a, b):
    sleep(5)
    return a + b


def minus_numbers(a, b):
    return a - b


if __name__ == "__main__":
    with Pool(processes=4) as pool:
        async_result_1 = pool.apply_async(add_numbers, args=(5, 3))
        async_result_2 = pool.apply_async(minus_numbers, args=(5, 3))
        while async_result_1.ready() == False:
            print(f'second task is finished and result is: {async_result_2.get()}')
            print('waiting first task .....')
        else:
            print(f'****** first task is finished, result is {async_result_1.get()} *****')
