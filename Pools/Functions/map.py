from multiprocessing import Pool


def safe_divide(x):
    return x / 5

if __name__== '__main__':
    with Pool(5) as pool:
        result = pool.map(safe_divide, [5,10,15,25,100])
    print(result)
