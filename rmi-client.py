# client.py

import socket

# Create socket
client = socket.socket()

# Connect to server
client.connect(('localhost', 5000))

# Input strings
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Send first string
client.send(str1.encode())

# Receive acknowledgment
client.recv(1024)

# Send second string
client.send(str2.encode())

# Receive result
result = client.recv(1024).decode()

print("Concatenated String:", result)

# Close connection
client.close()