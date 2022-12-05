with open("input5.txt") as f:
    idx = 0
    stacks = [[] for i in range(9)]
    while idx <= 8:
        l = f.readline()
        i = 0
        stack = 0
        while i < len(l):
            s = l[i : i + 3]
            if s[0] != " ":
                stacks[stack].insert(0, s[1])
            stack += 1
            i += 4
        idx += 1

    f.readline()
    lines = [x.strip().split(" ") for x in f.readlines()]

# task 1
# for line in lines:
#     n, start, end = [int(num) for num in [line[1], line[3], line[5]]]

#     while n > 0:
#         el = stacks[start - 1].pop()
#         stacks[end - 1].append(el)
#         n -= 1

# for stack in stacks:
#     print(stack.pop())

# task 2
for line in lines:
    n, start, end = [int(num) for num in [line[1], line[3], line[5]]]
    el = []
    while n > 0:
        el.append(stacks[start - 1].pop())
        n -= 1

    while len(el) > 0:
        stacks[end - 1].append(el.pop())


for stack in stacks:
    print(stack.pop())
