with open("input7.txt") as f:
    lines = [l.strip().split(" ") for l in f.readlines()]


curr_dir = []
size_of_dir = {}

for line in lines:
    if line[0] == "$" or line[0] == "dir":
        if line[1] == "cd":
            if line[2] == "..":
                curr_dir.pop()
            else:
                new_dir = curr_dir[-1] + line[2] + "/" if len(curr_dir) > 0 else line[2]
                curr_dir.append(new_dir)

        continue

    size = int(line[0])

    for d in curr_dir:
        size_of_dir[d] = size_of_dir.get(d, 0) + size


# task 1
output = sum(list(filter(lambda x: x <= 100000, size_of_dir.values())))

print(output)

# task 2
total_space = 70000000
used_space = size_of_dir["/"]
unused_space = 30000000
curr_space = total_space - used_space
min_delete_size = unused_space - curr_space

min_folder_size = min(
    list(filter(lambda x: x >= min_delete_size, size_of_dir.values()))
)

print(min_folder_size)
