file = open("input.txt", "r")
polymer_sequence = file.readline()
file.close()


i = 0
count = 1
while True:
    if count == 0:
        break
    count = 0
    i = 0
    while True:
        try:
            char1 = polymer_sequence[i]
            char2 = polymer_sequence[i + 1]
            if char1.lower() == char2.lower() and \
                    ((char1.islower() and char2.isupper()) or (char2.islower() and char1.isupper())):
                polymer_sequence = polymer_sequence.replace((char1 + char2), "", 1)
                count += 1
            i += 1
        except IndexError:
            break

print(len(polymer_sequence))
