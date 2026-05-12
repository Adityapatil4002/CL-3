# reducer.py

import sys

max_temp = -999
min_temp = 999

hot_year = ""
cool_year = ""

# Read mapper output
for line in sys.stdin:
    
    year, temp = line.strip().split('\t')

    temp = int(temp)

    # Find hottest year
    if temp > max_temp:
        max_temp = temp
        hot_year = year

    # Find coolest year
    if temp < min_temp:
        min_temp = temp
        cool_year = year

# Print result
print("Hottest Year :", hot_year, "Temperature :", max_temp)
print("Coolest Year :", cool_year, "Temperature :", min_temp)

# Sample Input File
# 2018 32
# 2019 40
# 2020 28
# 2021 45
# 2022 30

# Hadoop Commands
# Create Input Directory
# hdfs dfs -mkdir input
# Put Dataset File
# hdfs dfs -put weather.txt input
# Run MapReduce Job
# hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
# -file mapper.py \
# -mapper mapper.py \
# -file reducer.py \
# -reducer reducer.py \
# -input input/weather.txt \
# -output output
# View Output
# hdfs dfs -cat output/part-00000