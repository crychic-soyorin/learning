import multiprocessing
import time


def insert(array: list, value):
    for i in range(value):
        array.append(i)
        print(f"数组长度:{len(array)},array:{array}")
        time.sleep(1)


def read(array: list):
    while True:
        time.sleep(1)
        print(f"数组长度:{len(array)},array:{array}")


my_list = []
if __name__ == '__main__':
    p1 = multiprocessing.Process(target=insert, args=(my_list, 1000))
    p1.daemon = True
    p2 = multiprocessing.Process(target=read, kwargs={'array': my_list})
    p2.daemon = True
    p1.start()
    p2.start()
    time.sleep(2)
    print("主线程已结束...")
