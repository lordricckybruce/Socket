#!/bin/python3
import socket  #for low level networking
import threading  #increase the speed of scanning multiple ports

def scan_port(target_ip, port): #defines the function target ip and port
    try:  # to handle potentialn errors such as network issues
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #a tcp socket 
        sock.settimeout(1) #timeout is 1 second to reduce hanging
        result = sock.connect_ex((target_ip, port)) #the state of connection
        if result == 0:  #if return 0 connection is successful but if it doesn't connection is unsuccessful
            print(f"Port {port} is open")
        sock.close()  #closes socket to release system resources
    except Exception as e:  # where there is an error 
        print(f"Error scanning port {port}: {e}") # prints the error 

def scan_ports(target_ip, start_port, end_port): #defines the function: target ip, start_port, end_port
    print(f"Scanning {target_ip} from port {start_port} to {end_port}...") #print ip and port range being scanned 
    for port in range(start_port, end_port + 1):  #iterates through each port 
        thread = threading.Thread(target=scan_port, args=(target_ip, port))  #creates a new thread for connection
        thread.start()  #start the thread

if __name__ == "__main__":  # the following code is excecuted when  the scripts run directly 
    target_ip = input("Enter the target IP: ")
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))
    scan_ports(target_ip, start_port, end_port)
