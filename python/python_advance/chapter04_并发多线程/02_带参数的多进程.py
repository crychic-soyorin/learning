import multiprocessing
import os


def coding(name, num):
    for i in range(num + 1):
        print(f"{name}正在敲第{i + 1}遍代码")
    print(f"pid:{os.getpid()},{multiprocessing.current_process().pid},父进程id:{os.getppid()}")


def music(name, num):
    for i in range(num + 1):
        print(f"{name}正在听第{i + 1}遍音乐....")
    print(f"pid:{os.getpid()},{multiprocessing.current_process().pid},父进程id:{os.getppid()}")


if __name__ == '__main__':
    print(f"pid:{os.getpid()},{multiprocessing.current_process().pid},父进程id:{os.getppid()}")
    p1 = multiprocessing.Process(target=coding, args=('李四', 20))
    p2 = multiprocessing.Process(target=music, kwargs={"name": '张三', "num": 10})
    p1.start()
    p2.start()
