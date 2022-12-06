with open("input6.txt") as f:
    lines = f.readline()


def solution(size):
    curr = []
    for i in range(len(lines)):
        if len(curr) < size:
            curr.append(lines[i])
            continue

        curr.append(lines[i])
        curr.pop(0)

        if len(set(curr)) == size:
            print(i + 1)
            break


# part 1
solution(4)

# part 2
solution(14)
