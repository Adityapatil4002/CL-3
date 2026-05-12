# reducer.py

import sys

char_count = {}

# Read mapper output
for line in sys.stdin:
    
    char, count = line.strip().split('\t')
    
    count = int(count)

    # Store character count
    if char in char_count:
        char_count[char] += count
    else:
        char_count[char] = count

# Print final result
for char, total in char_count.items():
    print(f"{char}\t{total}")
    

# Commands to Run in Hadoop
# Create Input Folder
# hdfs dfs -mkdir input
# Put File in HDFS
# hdfs dfs -put data.txt input
# Run MapReduce Job
# hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
# -file mapper.py \
# -mapper mapper.py \
# -file reducer.py \
# -reducer reducer.py \
# -input input/data.txt \
# -output output
# View Output
# hdfs dfs -cat output/part-00000