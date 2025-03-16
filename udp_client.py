import socket
import time

def start_udp_client(server_host='127.0.0.1', server_port=12345, message_count=100):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    total_time = 0
    lost_packets = 0
    
    for i in range(message_count):
        message = f"Message {i+1}"
        start_time = time.time()
        client_socket.sendto(message.encode(), (server_host, server_port))
        
        client_socket.settimeout(0.001)  # Timeout for lost packets
        try:
            response, _ = client_socket.recvfrom(1024)
            end_time = time.time()
            round_trip_time = end_time - start_time
            total_time += round_trip_time
            print(f"Sent: {message}, Received: {response.decode()}, Round-trip time: {round_trip_time:.6f} seconds")
        except socket.timeout:
            lost_packets += 1
            print(f"Message {i+1} lost")
    
    received_packets = message_count - lost_packets
    average_latency = total_time / received_packets if received_packets > 0 else 0
    packet_loss_rate = (lost_packets / message_count) * 100
    throughput = received_packets / total_time if total_time > 0 else 0
    
    print(f"Average Latency: {average_latency:.6f} seconds")
    print(f"Packet Loss Rate: {packet_loss_rate:.2f}%")
    print(f"Throughput: {throughput:.2f} messages per second")
    
    client_socket.close()

if __name__ == "__main__":
    start_udp_client()
