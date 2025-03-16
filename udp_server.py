import socket
import random

def start_udp_server(host='0.0.0.0', port=12345, packet_loss_chance=0.1):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    print(f"UDP Server listening on {host}:{port}")
    
    while True:
        data, addr = server_socket.recvfrom(1024)
        message = data.decode()
        
        if random.random() > packet_loss_chance:
            response = f"Received: {message}"
            server_socket.sendto(response.encode(), addr)
            print(f"Processed message '{message}' from {addr}")
        else:
            print(f"Dropped message '{message}' from {addr}")

if __name__ == "__main__":
    start_udp_server()
