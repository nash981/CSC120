from time import *


def sum_time(array):
    sum1 = 0
    start = time()
    for i in range(len(array)):
        sum1 += array[i]
    end = time()
    print(end - start)
    print(len(array))


def main():
    arr = []
    for i in range(10000000):
        arr += [1,2,3,4,5,6,7,8,9,10]
    sum_time(arr)


if __name__ == '__main__':
    main()


"""
0.07178497314453125
1000000
0.7869081497192383
10000000
7.250673055648804
100000000
"""