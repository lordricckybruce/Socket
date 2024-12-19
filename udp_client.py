#!/bin/python3
import socket

def start_udp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.sendto(b'Hello UDP Server!', ('localhost', 9090))
    message, server_address = client_socket.recvfrom(1024)
    print(f"Received from server: {message.decode()}")
    client_socket.close()

if __name__ == "__main__":
    start_udp_client()
