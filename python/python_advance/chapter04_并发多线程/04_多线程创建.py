import threading


def coding(name, line):
    for i in range(line):
        print(f"{name}正在写第{i + 1}行代码...")


def music(name):
    print(f"{name}正在听音乐...")


# if __name__ == '__main__':
#     t1 = threading.Thread(target=coding, args=('zhangsan', 20))
#     t2 = threading.Thread(target=music, args=('zhangsan',))
#     t1.start()
#     t2.start()

t1 = threading.Thread(target=coding, args=('zhangsan', 20))
t2 = threading.Thread(target=music, args=('zhangsan',))
t1.start()
t2.start()
