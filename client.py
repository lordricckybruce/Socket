#!/bin/python3
import socket
'''
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 8080))
message = client.recv(1024)
print(f'Received from server: {message.decode()}')
client.close()
'''
def tcp_client():
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect(('locahost', 6606))
	message = client.recv(1024)
	print(f'Received from server: {message.decode()}')
	client.close()
if __name__ == "__main__":
	tcp_client()
