# mapper.py

import sys

# Read input line by line
for line in sys.stdin:
    
    # Split words
    words = line.strip().split()

    # Emit each word with 1
    for word in words:
        print(f"{word}\t1")