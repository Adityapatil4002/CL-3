# mapper.py

import sys

# Read input data
for line in sys.stdin:
    
    # Split year and temperature
    year, temp = line.strip().split()

    # Send data to reducer
    print(f"{year}\t{temp}")