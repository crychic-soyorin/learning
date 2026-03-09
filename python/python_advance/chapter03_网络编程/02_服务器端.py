import socket

# 创建socket对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定ip和端口号
server_socket.bind(('localhost', 9999))
# 开始监听
server_socket.listen(5)
# 等待连接
accept_socket, client_info = server_socket.accept()
# 给客户端发送消息
accept_socket.send(b'Welcome to socket')
# 接收客户端的消息并打印
data=accept_socket.recv(1024).decode("utf-8")
print(f"服务器端收到：{data},来自客户端：{client_info}")
# 关闭
accept_socket.close()
# 服务器关闭，一般不关服务器
# server_socket.close()
