from socket import socket, AF_INET, SOCK_DGRAM
import time


IP = '192.168.88.160'
PORT = 8888
addr = (IP, PORT)

udp_socket = socket(AF_INET, SOCK_DGRAM)


for i in range(1, 16):
    for j in range(1, 16):
        udp_socket.sendto(f'DRW;{i};{j}'.encode(), addr)
        time.sleep(0.01)

time.sleep(10)
udp_socket.sendto('CLR'.encode(), addr)
udp_socket.close()