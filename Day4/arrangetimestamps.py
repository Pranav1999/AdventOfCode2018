import re
import numpy as np

np.set_printoptions(threshold=np.nan)

file = open("input.txt", "r")
timestamps = file.readlines()
timestamps.sort()
file.close()
file = open("timestamps.txt", "w")
file.writelines(timestamps)
file.close()