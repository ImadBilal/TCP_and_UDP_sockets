import socket
import time

def start_server(host='0.0.0.0', port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")
    
    conn, addr = server_socket.accept()
    print(f"Connection established with {addr}")
    
    while True:
        start_time = time.time()
        message = conn.recv(1024).decode()
        if not message:
            break
        response = f"Received: {message}"
        conn.send(response.encode())
        end_time = time.time()
        print(f"Processed message '{message}' in {end_time - start_time:.6f} seconds")
    
    conn.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()
