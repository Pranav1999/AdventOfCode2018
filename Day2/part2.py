import jellyfish

file = open("input.txt", "r")
ids = file.readlines()


def similar_id_index():
    for i in range(0, len(ids)):
        for j in range(i + 1, len(ids)):
            if jellyfish.levenshtein_distance(ids[i], ids[j]) == 1:
                return list([i, j])


def print_common_letters(i, j):
    for k in range(0, len(ids[0])):
        if ids[i][k] == ids[j][k]:
            print(ids[i][k], end="")


common_ids = similar_id_index()
print_common_letters(common_ids[0], common_ids[1])
