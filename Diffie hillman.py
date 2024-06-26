server

import socket

HOST = '192.168.56.1'  # Listen on all available network interfaces
PORT = 12345  # Choose a port number (make sure it's not already in use)

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the host and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen()

print(f"Server listening on {HOST}:{PORT}")

while True:
    # Accept incoming connections
    client_socket, client_address = server_socket.accept()

    print(f"Connection from {client_address}")

    a = int(input("Enter a : "))
    b = int(input("Enter b : "))
    x = int(input("Enter x : "))
    public_key = (a**x) % b
    client_socket.sendall(f"{public_key}".encode())
    received_key = int(client_socket.recv(1024).decode())
    shared_key = (received_key**x) % b
    print("Shared key : ", shared_key)

    # Receive and send messages in a loop
    while True:
        data = client_socket.recv(1024)
        if not data:
            # If no more data is received, break the inner loop
            client_socket.close()
            break
        print(f"Received data from {client_address}: {data.decode()}")
        
        # You can add your processing logic here
        
        # Echo the received data back to the client
        response = input("Enter response: ")
        client_socket.sendall(response.encode())

# Close the server socket (this line will not be reached in the current setup)
server_socket.close()
------------------------------------------------------
client:

import socket

HOST = '192.168.56.1'
PORT = 12345

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))

# Send public key to the server
a = int(input("Enter a: "))
b = int(input("Enter b: "))
x = int(input("Enter x: "))
public_key = (a**x) % b
client_socket.sendall(f"{public_key}".encode())

# Receive modified key from the server
received_key = int(client_socket.recv(1024).decode())
private_key = (received_key**x) % b
print("Shared key is", private_key)

# Send and receive messages in a loop
while True:
    # Send data to the server
    message = input("Enter message to send (type 'exit' to quit): ")
    if message.lower() == 'exit':
        break
    client_socket.sendall(message.encode())

    # Receive response from the server
    response = client_socket.recv(1024)
    print(f"Received response from server: {response.decode()}")

# Close the client socket
client_socket.close()

----------------------------------------------------
input output:
server:
Connection from ('192.168.56.1', 59929)
Enter a : 1
Enter b : 2
Enter x : 5
Shared key :  1
Received data from ('192.168.56.1', 59929): naina
Enter response: Sharma

client:
Enter a: 1
Enter b: 2
Enter x: 3
Shared key is 1
Enter message to send (type 'exit' to quit): naina
Received response from server: sharma
Enter message to send (type 'exit' to quit):
