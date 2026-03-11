import threading
import time


def insert(list, value):
    for i in range(value):
        time.sleep(0.1)
        list.append(i)


def read(list, value):
    for i in range(value):
        time.sleep(0.1)
        print(f"list长度:{len(list)},list:{list}")


array = []
t1 = threading.Thread(target=insert, args=(array, 10))
t2 = threading.Thread(target=read, args=(array, 10))

t1.start()
t2.start()
