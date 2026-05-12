# mapper.py

import sys

# Read input line by line
for line in sys.stdin:
    
    # Remove spaces and newline
    line = line.strip().replace(" ", "")
    
    # Emit each character with count 1
    for char in line:
        print(f"{char}\t1")