# TCP_and_UDP_sockets
This repository will record and compare the rtt, throughput, average latency and packet loss in tcp and udp communication.

### How to run:
First run the server file and then run their respective client file. 

### Expected outputs:
  Run the server file:
  
    Server listening on 0.0.0.0:12345
  
  Run TCP client file:
  
    Sent: Message 1, Received: Received: Message 1, Round-trip time: 0.000000 seconds
    Sent: Message 2, Received: Received: Message 2, Round-trip time: 0.000180 seconds
                      .
                      .
                      .
    Sent: Message 100, Received: Received: Message 100, Round-trip time: 0.000000 seconds
    Average Latency: 0.000037 seconds
    Throughput: 27365.46 messages per second

  
Run UDP client file:

    Sent: Message 1, Received: Received: Message 1, Round-trip time: 0.000988 seconds
    Message 2 lost
    Sent: Message 3, Received: Received: Message 3, Round-trip time: 0.000461 seconds
                      .
                      .
                      .
    Sent: Message 100, Received: Received: Message 100, Round-trip time: 0.000000 seconds
    Average Latency: 0.000142 seconds
    Packet Loss Rate: 12.00%
    Throughput: 7060.71 messages per second

### 







