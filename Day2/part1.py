file = open("input.txt")
ids = file.readlines()

# for exactly two or three of any letters
count_three = 0
count_two = 0
for id in ids:
    flag_two = True
    flag_three = True
    for char in id:
        if id.count(char) == 2 and flag_two:
            count_two += 1
            flag_two = False
        if id.count(char) == 3 and flag_three:
            count_three += 1
            flag_three = False
        if not (flag_three or flag_two):
            break

checksum = count_three * count_two
print(checksum)
