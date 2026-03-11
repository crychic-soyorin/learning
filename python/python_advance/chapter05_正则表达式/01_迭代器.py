class MyIterator:
    def __init__(self, start, end):
        self.current_value = start
        self.end_value = end

    # 重写迭代器对象，返回当前对象，迭代器对象
    def __iter__(self):
        return self

    # 返回当前值，并更新当前值
    def __next__(self):
        if self.current_value >= self.end_value:
            # 抛出异常停止迭代
            raise StopIteration
        self.current_value += 1
        return self.current_value - 1


for i in MyIterator(1, 6):
    print(i)

