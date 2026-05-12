# Simple DEAP Example

from deap import base, creator, tools
import random

# Create Fitness Function
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()

# Generate random number
toolbox.register("attr_int", random.randint, 0, 10)

# Create individual
toolbox.register("individual", tools.initRepeat,
                 creator.Individual, toolbox.attr_int, 5)

# Create population
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Fitness Function
def fitness(individual):
    return (sum(individual),)

toolbox.register("evaluate", fitness)

# Population
pop = toolbox.population(n=5)

# Evaluate Fitness
for ind in pop:
    ind.fitness.values = toolbox.evaluate(ind)

# Print Results
for ind in pop:
    print(ind, "Fitness =", ind.fitness.values[0])

# Best Individual
best = tools.selBest(pop, 1)

print("\nBest Individual:", best[0])