file = open("input.txt", "r")
changes = file.readlines()

result = 0
for change in changes:
    result += int(change)

print(result)
