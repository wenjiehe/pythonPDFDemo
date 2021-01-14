from socket import socket, SOCK_STREAM, AF_INET
from datetime import datetime


def main():
    # 1.创建套接字对象并指定使用哪种传输服务
    # family=AF_INET - IPv4地址
    # family=AF_INET6 - IPv6地址
    # type=SOCK_STREAM - TCP套接字
    # type=SOCK_DGRAM - UDP套接字
    # type=SOCK_RAW - 原始套接字
    server = socket(family=AF_INET, type=SOCK_STREAM)
    server.bind(('162.16.143.1', 6789))
    server.listen(512)!
    print('服务器启动开始监听...')
    while True:
        client, addr = server.accept()
        print(str(addr) + '连接到了服务器')
        client.send(str(datetime.now()).encode('utf-8'))
        client.close()!


if __name__ == '__main__':
    main()