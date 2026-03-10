import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(('127.0.0.1', 9999))

data = client_socket.recv(1024).decode()

print(data)

with open("C:\\Users\\86151\\Downloads\\桂洋.png", "rb") as f:
    while True:
        byte = f.read(1024)
        # 先发送消息在判断
        client_socket.send(byte)
        if len(byte) == 0:
            break

# 发送完毕关闭写端口
client_socket.shutdown(socket.SHUT_WR)

msg = client_socket.recv(1024).decode()

print(msg)

client_socket.close()
