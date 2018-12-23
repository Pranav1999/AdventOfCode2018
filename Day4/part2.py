import re
import numpy as np

np.set_printoptions(threshold=np.nan)

file = open("timestamps.txt", "r")
timestamps = file.readlines()
file.close()

records = np.zeros((267, 61), dtype=int)

i = 0
j = 0
while i < len(timestamps):
    regex = re.compile(r"#\d*")
    id = regex.search(timestamps[i])
    id = id.group()[1:]
    records[j][0] = id
    i += 1
    while True:
        try:
            if timestamps[i][19:24] == "falls":
                regex = re.compile(r"\d\d:\d\d")
                sleep_time = regex.search(timestamps[i])
                sleep_time = sleep_time.group()
                sleep_time = sleep_time.split(":")
                sleep_time = sleep_time[1]
                awake_time = regex.search(timestamps[i + 1])
                awake_time = awake_time.group()
                awake_time = awake_time.split(":")
                awake_time = awake_time[1]
                sleep_time = int(sleep_time)
                awake_time = int(awake_time)
                i += 2
                for k in range(sleep_time + 1, awake_time + 1):
                    records[j][k] = 1
            else:
                break
        except IndexError:
            break

    j += 1

idrecords = {}

for i in range(267):
    if not idrecords.get(records[i][0]) is None:
        temp = idrecords.get(records[i][0])
        for j in range(1, 61):
            temp[j - 1] = temp[j - 1] + records[i][j]
        idrecords[records[i][0]] = temp
    else:
        idrecords[records[i][0]] = records[i][1:]


def most_sleep(idrecords):
    most_sleep_id = 0
    most_sleep_minute_time = 0
    most_sleep_minute = 0
    for i in range(60):
        for k in idrecords.keys():
            if most_sleep_minute_time < idrecords[k][i]:
                most_sleep_minute_time = idrecords[k][i]
                most_sleep_minute = i
                most_sleep_id = k

    return [most_sleep_id, most_sleep_minute]


solution = most_sleep(idrecords)

print("solution: ", (solution[0] * solution[1]))
