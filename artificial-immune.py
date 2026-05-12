# Artificial Immune Pattern Recognition
# Structure Damage Classification

# Training Data
# 0 = No Damage
# 1 = Damage

data = [
    [2, 3, 0],
    [3, 4, 0],
    [7, 8, 1],
    [8, 9, 1]
]

# Input Structure Values
test = [6, 7]

best_match = None
minimum_distance = 999

# Find nearest antibody
for row in data:
    distance = ((test[0] - row[0])**2 + (test[1] - row[1])**2) ** 0.5

    if distance < minimum_distance:
        minimum_distance = distance
        best_match = row[2]

# Result
if best_match == 1:
    print("Structure Damage Detected")
else:
    print("No Structure Damage")