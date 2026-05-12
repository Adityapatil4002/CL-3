# load_balancer.py

# List of servers
servers = ["Server 1", "Server 2", "Server 3"]

# Client requests
requests = ["Req1", "Req2", "Req3", "Req4", "Req5", "Req6"]

server_index = 0

print("Load Balancing Simulation\n")

# Assign requests to servers
for request in requests:
    
    print(request, "assigned to", servers[server_index])

    # Move to next server
    server_index = (server_index + 1) % len(servers)