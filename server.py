#!/bin/python3
import socket
'''
server =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 8080))
server.listen(6)
print("TCP server is listening on port 8080")
while True:
	client_socket, client_address =  server.accept()
	print(f"Connection established with {client_address} successful")
	client_socket.send(b'Hola Andreas')
	client_socket.close()
'''
def tcp_server():
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind(('localhost', 6606))
	server.listen(19)
	print("TCP server listening on port 6606")
	while True:
		client_socket, client_address =  server.accept()
		print(f'Connection established with {client_address}')
		client_socket.send(b'Hola amigo from la cruise ')
		client_socket.close()
if __name__ == "__main__":
	tcp_server()
