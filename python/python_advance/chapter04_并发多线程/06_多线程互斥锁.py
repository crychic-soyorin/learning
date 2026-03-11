import threading

global_num = 0
mutex = threading.Lock()


def add():
    global global_num
    # 上锁
    mutex.acquire()
    for i in range(10000000):
        global_num += 1
    print(global_num)
    # 解锁
    mutex.release()


t1 = threading.Thread(target=add)
t2 = threading.Thread(target=add)

t1.start()
t2.start()
