file = open("input.txt", "r")
changes = file.readlines()

run = True

frequencies = set()
result = 0
frequencies.add(result)
while run:
    for change in changes:
        result += int(change)
        if result in frequencies:
            print(result)
            run = False
            break
        frequencies.add(result)
