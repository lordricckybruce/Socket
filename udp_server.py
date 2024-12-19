#!/bin/python3
import socket

def start_udp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('localhost', 9090))
    print("UDP Server listening on port 9090")

    while True:
        message, client_address = server_socket.recvfrom(1024)
        print(f"Message from {client_address}: {message.decode()}")
        server_socket.sendto(b'Hello from UDP Server!', client_address)

if __name__ == "__main__":
    start_udp_server()

'''
udp uses dgram in place of tcp sock stream
recvfrom in place of accept
'''
