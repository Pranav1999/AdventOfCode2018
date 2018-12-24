file = open("input.txt", "r")
polymer_sequence = file.readline()
file.close()

unique_units = set()
for ch in polymer_sequence:
    unique_units.add(ch.lower())

print(unique_units)

shortest_polymer = ""
shortest_polymer_len = 1000000

for unique_unit in unique_units:
    temp_polymer_sequence = polymer_sequence.replace(unique_unit, "").replace(unique_unit.upper(), "")
    i = 0
    count = 1
    while True:
        if count == 0:
            break
        count = 0
        i = 0
        while True:
            try:
                char1 = temp_polymer_sequence[i]
                char2 = temp_polymer_sequence[i + 1]
                if char1.lower() == char2.lower() and \
                        ((char1.islower() and char2.isupper()) or (char2.islower() and char1.isupper())):
                    temp_polymer_sequence = temp_polymer_sequence.replace((char1 + char2), "", 1)
                    count += 1
                i += 1
            except IndexError:
                break

    if len(temp_polymer_sequence) < shortest_polymer_len:
        shortest_polymer = temp_polymer_sequence
        shortest_polymer_len = len(temp_polymer_sequence)

print(shortest_polymer_len)
