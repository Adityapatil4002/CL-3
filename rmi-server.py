# server.py

import socket

# Create socket
server = socket.socket()

# Bind host and port
server.bind(('localhost', 5000))

# Listen for client
server.listen(1)

print("Server is waiting for connection...")

# Accept connection
conn, addr = server.accept()

print("Connected to:", addr)

# Receive first string
str1 = conn.recv(1024).decode()

# Send acknowledgment
conn.send("Received first string".encode())

# Receive second string
str2 = conn.recv(1024).decode()

# Concatenate strings
result = str1 + str2

# Send result to client
conn.send(result.encode())

print("Concatenated string sent")

# Close connection
conn.close()
server.close()