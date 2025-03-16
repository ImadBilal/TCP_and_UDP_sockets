import socket
import time

def start_client(server_host='127.0.0.1', server_port=12345, message_count=100):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))
    
    total_time = 0
    for i in range(message_count):
        message = f"Message {i+1}"
        start_time = time.time()
        client_socket.send(message.encode())
        response = client_socket.recv(1024).decode()
        end_time = time.time()
        round_trip_time = end_time - start_time
        total_time += round_trip_time
        print(f"Sent: {message}, Received: {response}, Round-trip time: {round_trip_time:.6f} seconds")
    
    average_latency = total_time / message_count
    throughput = message_count / total_time if total_time > 0 else 0
    print(f"Average Latency: {average_latency:.6f} seconds")
    print(f"Throughput: {throughput:.2f} messages per second")
    
    client_socket.close()

if __name__ == "__main__":
    start_client()
