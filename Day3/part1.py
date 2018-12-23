import re
import numpy as np

np.set_printoptions(threshold=np.nan)

file = open("input.txt", "r")
claims = file.readlines()

left_edge = 0
top_edge = 0
rows = 0
columns = 0

fabric = np.zeros((1000, 1000))

for claim in claims:
    edges_regex = re.compile(r'\d+,\d+')
    edge_match = edges_regex.search(claim)
    edge_match = edge_match.group().split(',')
    left_edge = edge_match[0]
    top_edge = edge_match[1]
    size_regex = re.compile(r'\d+x\d+')
    size_match = size_regex.search(claim)
    size_match = size_match.group().split('x')
    rows = size_match[0]
    columns = size_match[1]
    left_edge = int(left_edge)
    top_edge = int(top_edge)
    rows = int(rows)
    columns = int(columns)

    for i in range((left_edge - 1), (left_edge + rows - 1)):
        for j in range((top_edge - 1), (top_edge + columns - 1)):
            fabric[i][j] += 1

count = 0
for i in range(1000):
    for j in range(1000):
        if fabric[i][j] > 1:
            count += 1

print(count)
