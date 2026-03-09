s1 = "网络编程"
# 默认编码UTF-8
print(s1.encode())
print(s1.encode("gb2312"))
print(s1.encode("utf-8"))
print(s1.encode("gbk"))

bytes = b'\xe7\xbd\x91\xe7\xbb\x9c\xe7\xbc\x96\xe7\xa8\x8b'
print(bytes.decode("utf-8"))
