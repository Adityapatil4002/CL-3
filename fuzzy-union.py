# Fuzzy Sets Operations

A = {'x1': 0.2, 'x2': 0.5, 'x3': 0.7}
B = {'x1': 0.6, 'x2': 0.4, 'x3': 0.8}

print("Set A:", A)
print("Set B:", B)

# Union
union = {}
for i in A:
    union[i] = max(A[i], B[i])

print("\nUnion:", union)

# Intersection
intersection = {}
for i in A:
    intersection[i] = min(A[i], B[i])

print("Intersection:", intersection)

# Complement
comp_A = {}
for i in A:
    comp_A[i] = 1 - A[i]

print("Complement of A:", comp_A)

# Difference A - B
difference = {}
for i in A:
    difference[i] = min(A[i], 1 - B[i])

print("Difference A-B:", difference)


# Cartesian Product (Fuzzy Relation)
R = {}

for i in A:
    for j in B:
        R[(i, j)] = min(A[i], B[j])

print("\nFuzzy Relation R (Cartesian Product):")
for k, v in R.items():
    print(k, ":", v)


# Another Fuzzy Relation S
S = {
    ('x1', 'y1'): 0.3,
    ('x1', 'y2'): 0.7,
    ('x2', 'y1'): 0.6,
    ('x2', 'y2'): 0.5,
    ('x3', 'y1'): 0.8,
    ('x3', 'y2'): 0.4
}

T = {
    ('y1', 'z1'): 0.5,
    ('y1', 'z2'): 0.9,
    ('y2', 'z1'): 0.7,
    ('y2', 'z2'): 0.3
}

# Max-Min Composition
result = {}

X = ['x1', 'x2', 'x3']
Y = ['y1', 'y2']
Z = ['z1', 'z2']

for x in X:
    for z in Z:
        values = []
        for y in Y:
            values.append(min(S[(x, y)], T[(y, z)]))
        result[(x, z)] = max(values)

print("\nMax-Min Composition:")
for k, v in result.items():
    print(k, ":", v)