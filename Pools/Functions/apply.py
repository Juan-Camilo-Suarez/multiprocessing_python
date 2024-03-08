from multiprocessing import Pool

"""
- function apply is used to define task for one of the process 
- for any of the processes
- the execution block the processes work until the result is ready.
"""

def get_module(x):
    return x % 2


if __name__ == '__main__':
    with Pool(5) as pool:
        result = pool.apply(get_module, (85, ))
        print(result)
