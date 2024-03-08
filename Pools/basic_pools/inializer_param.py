# this file contains example how use inializer param in pool
from multiprocessing import Pool

# the initializer param is used to define initital varibles or configs for every process before of beging
def initializer(x):
    global y
    y = x


def worker(n):
    return n * y


if __name__ == '__main__':
    with Pool(initializer=initializer, initargs=(10,)) as pool:
        results = pool.map(worker, range(10))

    print(results)
