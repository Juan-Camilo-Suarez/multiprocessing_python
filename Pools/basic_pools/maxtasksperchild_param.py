# this file contains example how use maxtasksperchild param in pool
import os
from multiprocessing import Pool


def worker(n):
    current_process_id = os.getpid()
    return n * n, current_process_id


if __name__ == '__main__':
    with Pool(maxtasksperchild=10) as pool:
        results = pool.map(worker, range(100))
        for result, process_id in results:
            print(f"Result: {result}, Process ID: {process_id}")

    print(results)

    # ****** whit defined processes
    # if __name__ == '__main__':
    #   with Pool(processes=2, maxtasksperchild=10) as pool:
    #     results = pool.map(worker, range(100))
    #     for result, process_id in results:
    #         print(f"Result: {result}, Process ID: {process_id}")
    #
    #   print(results)
