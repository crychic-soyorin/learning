import multiprocessing


def coding():
    for i in range(10):
        print(f"正在敲第{i + 1}遍代码")


def music():
    for i in range(10):
        print(f"正在听第{i + 1}遍音乐....")


# coding()
# music()

# 启动进程
if __name__ == '__main__':
    p1 = multiprocessing.Process(target=coding)
    p2 = multiprocessing.Process(target=music)

    p1.start()
    p2.start()
