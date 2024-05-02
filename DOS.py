SERVER:

import socket
import logging

# Setup basic logging
logging.basicConfig(level=logging.INFO)

HOST = '0.0.0.0'  # Listen on all available network interfaces
PORT = 12345  # Choose a port number (make sure it's not already in use)

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# This option helps in reusing the same port (helpful after a server restart)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind the socket to the host and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen()
logging.info(f"Server listening on {HOST}:{PORT}")

try:
    while True:  # Main loop to accept incoming connections
        client_socket, client_address = server_socket.accept()
        logging.info(f"Connection from {client_address}")

        try:
            while True:  # Loop to handle continuous communication
                # Example of receiving data (you can adjust according to your needs)
                data = client_socket.recv(1024)
                if not data:
                    break  # Break the loop if no data is received
                logging.info(f"Received data from {client_address}: {data.decode()}")

                # Example sending data back - echo (you can adjust this part)
                client_socket.sendall(data)
        except Exception as e:
            logging.error(f"An error occurred: {e}")
        finally:
            client_socket.close()  # Make sure to close the client socket

except KeyboardInterrupt:
    logging.info("Server is shutting down.")
finally:
    server_socket.close()  # Ensure the server socket is closed on exit


------------------------------------------------------------------------
Client:

import socket
import time

def ping_server(host, port, num_pings):
    # Calculate the sleep duration to distribute the pings across one second
    sleep_duration = 1.0 / num_pings if num_pings > 0 else 0

    while True:  # Start an infinite loop
        for _ in range(num_pings):
            start_time = time.time()

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                try:
                    s.connect((host, port))
                    # You can modify this message to be whatever you'd like
                    message = "ping"
                    s.sendall(message.encode())
                    data = s.recv(1024)
                    print(f"Received: {data.decode()}")
                except Exception as e:
                    print(f"An error occurred: {e}")

            # Calculate the actual time taken to send a ping and adjust the sleep time
            elapsed_time = time.time() - start_time
            adjusted_sleep_duration = max(0, sleep_duration - elapsed_time)
            time.sleep(adjusted_sleep_duration)
        # This sleep ensures the loop runs once per second, adjust as needed
        time.sleep(1 - num_pings * sleep_duration)

# Replace '192.168.207.182' and 12345 with your server's IP and port
HOST = '192.168.74.129'  
PORT = 12345
NUM_PINGS = int(input("Enter how many times to ping per second: "))

ping_server(HOST, PORT, NUM_PINGS)
