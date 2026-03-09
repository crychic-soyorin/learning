import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('localhost', 9999))

server_socket.listen(5)

server, client_info = server_socket.accept()

server.send("可以开始文件传输了...".encode())

with open("D:\\mydata.png", "ab") as f:
    while True:
        byte = server.recv(1024)
        f.write(byte)
        if len(byte) == 0:
            break

server.send("文件上传完毕...".encode())

server.close()
