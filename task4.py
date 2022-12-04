with open("input4.txt") as f:
    lines = [x.strip().split(",") for x in f.readlines()]

# part 1
total = 0
intersects = 0
for first, second in lines:

    start_1, end_1 = [int(num) for num in first.split("-")]
    start_2, end_2 = [int(num) for num in second.split("-")]

    s_1 = set([i for i in range(start_1, end_1 + 1)])
    s_2 = set([i for i in range(start_2, end_2 + 1)])

    if s_2.issubset(s_1) or s_1.issubset(s_2):
        total += 1

    if s_2.intersection(s_1):
        intersects += 1

print(total)
print(intersects)
