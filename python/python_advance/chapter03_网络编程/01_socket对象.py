"""
socket对象的创建
"""
import socket

# 创建Socket对象
# 地址族 AF_INET:IPV4 AF_INET6:IPV6
# 通信方式 SOCK_STREAM:TCP协议 SOCK_DGRAM:UDP协议
socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(socket_obj)
