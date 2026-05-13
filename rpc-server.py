# server.py

import socket

# Create socket
server = socket.socket()

# Bind host and port
server.bind(('localhost', 5000))

# Start listening
server.listen(1)

print("Server is waiting...")

# Accept client connection
conn, addr = server.accept()

print("Connected to:", addr)

# Receive number from client
num = int(conn.recv(1024).decode())

# Calculate factorial
fact = 1

for i in range(1, num + 1):
    fact *= i

