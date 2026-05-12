import random

# Distance Matrix
distance = [
    [0, 2, 9, 10],
    [1, 0, 6, 4],
    [15, 7, 0, 8],
    [6, 3, 12, 0]
]

cities = [0, 1, 2, 3]

best_path = []
best_cost = 999

# Simple Ant Colony Simulation
for i in range(5):   # number of ants

    path = cities[:]
    random.shuffle(path)

    cost = 0

    for j in range(len(path)-1):
        cost += distance[path[j]][path[j+1]]

    # return to starting city
    cost += distance[path[-1]][path[0]]

    print("Path:", path, "Cost:", cost)

    if cost < best_cost:
        best_cost = cost
        best_path = path

print("\nBest Path:", best_path)
print("Minimum Cost:", best_cost)