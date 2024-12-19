import socket  # provides low-level networking capabilites, creating connections and handling sockets

def scan_ports(target_ip): #funct: target ip
    print(f"Scanning {target_ip} for open ports...")
    open_ports = []
    for port in range(1, 1025): #iterates from 1 1025
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creates a tcp socket using ipv4
        sock.settimeout(1) #sets a time out of 1secs to avoid hanging
        result = sock.connect_ex((target_ip, port)) #if connection is successsful
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

if __name__ == "__main__":
    target_ip = '192.168.1.1'
    open_ports = scan_ports(target_ip)
    print(f"Open ports on {target_ip}: {open_ports}")
