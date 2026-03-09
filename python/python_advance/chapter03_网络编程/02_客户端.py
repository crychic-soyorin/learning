import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(('127.0.0.1', 9999))

data = client_socket.recv(1024).decode('utf-8')

print(f'接收到服务端消息:{data}')

client_socket.send(b'hello world')

client_socket.close()
