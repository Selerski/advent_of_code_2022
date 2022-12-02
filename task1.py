with open("input.txt") as f:
    lines = list(
        map(lambda x: x if x == "" else int(x), [x.strip() for x in f.readlines()])
    )


highest_cals = 0
curr = 0
highest_nums = []


for i in range(len(lines)):
    if lines[i] == "" or i == len(lines) - 1:
        highest_nums.append(curr)
        highest_nums.sort(reverse=True)

        if (len(highest_nums)) > 3:
            highest_nums.pop()

        if curr >= highest_cals:
            highest_cals = curr

        curr = 0
    else:
        curr += lines[i]

print(highest_cals)
print(sum(highest_nums))
