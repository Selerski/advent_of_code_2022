from string import ascii_lowercase, ascii_uppercase

with open("input3.txt") as f:
    lines = [x.strip() for x in f.readlines()]

lower_mappings = {val: idx + 1 for idx, val in enumerate(ascii_lowercase)}
higher_mappings = {val: idx + 27 for idx, val in enumerate(ascii_uppercase)}


def get_total(inp):
    return lower_mappings[inp] if inp in ascii_lowercase else higher_mappings[inp]


# part1
total = 0
for line in lines:
    mid = len(line) // 2
    uniq_1 = set(line[0:mid])
    uniq_2 = set(line[mid : len(line)])

    intersection = uniq_1.intersection(uniq_2).pop()

    total += get_total(intersection)
print(total)

# part2
total = 0
for i in range(0, len(lines), 3):
    uniq_1 = set(lines[i])
    uniq_2 = set(lines[i + 1])
    uniq_3 = set(lines[i + 2])
    intersection = uniq_1.intersection(uniq_2).intersection(uniq_3).pop()

    total += get_total(intersection)


print(total)
