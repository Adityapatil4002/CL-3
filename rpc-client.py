# client.py

import socket

# Create socket
client = socket.socket()

# Connect to server
client.connect(('localhost', 5000))

# Input number
num = input("Enter a number: ")

# Send number to server
client.send(num.encode())

# Receive factorial from server
result = client.recv(1024).decode()

print("Factorial is:", result)

# Close connection
client.close()