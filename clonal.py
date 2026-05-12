import random

# Initial antibodies
population = [random.randint(1, 100) for i in range(5)]

print("Initial Population:", population)

# Fitness Function (Target = 50)
def fitness(x):
    return abs(50 - x)

# Sort according to fitness
population.sort(key=fitness)

print("\nBest Antibody:", population[0])

# Cloning
clones = [population[0]] * 3

print("Clones:", clones)

# Mutation
mutated = []

for i in clones:
    mutated.append(i + random.randint(-5, 5))

print("Mutated Clones:", mutated)

# Select Best
best = min(mutated, key=fitness)

print("\nFinal Best Solution:", best)