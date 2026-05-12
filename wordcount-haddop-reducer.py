# reducer.py

import sys

word_count = {}

# Read mapper output
for line in sys.stdin:
    
    word, count = line.strip().split('\t')
    
    count = int(count)

    # Count occurrences
    if word in word_count:
        word_count[word] += count
    else:
        word_count[word] = count

# Print result
for word, total in word_count.items():
    print(f"{word}\t{total}")
    
    
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