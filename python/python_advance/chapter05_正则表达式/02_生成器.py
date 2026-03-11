# 生成器 推导式写法 生成1-10之间的整数
my_generator = [i for i in range(10)]
print(my_generator)
my_generator = {i for i in range(10)}
print(my_generator)
# <generator object <genexpr> at 0x0000020DA95E5A80>
my_generator = (i for i in range(10) if i % 2 == 0)
print(my_generator)

# 如何从生成器中获取数据
for i in my_generator:
    print(i)
