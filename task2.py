with open("input2.txt") as f:
    lines = [x.strip().split(" ") for x in f.readlines()]


# part 1
score_map = {"X": 1, "Y": 2, "Z": 3}
equal_map = {"X": "A", "Y": "B", "Z": "C"}


def is_win(you, opponent):
    return (
        (you == "X" and opponent == "C")
        or (you == "Y" and opponent == "A")
        or (you == "Z" and opponent == "B")
    )


def is_draw(you, opponent):
    return equal_map[you] == opponent


total = 0
for opponent, you in lines:
    total += score_map[you]

    if is_draw(you, opponent):
        total += 3
    elif is_win(you, opponent):
        total += 6
    else:
        total += 0

print(total)


win_map = {"A": "B", "B": "C", "C": "A"}
loss_map = {"A": "C", "B": "A", "C": "B"}
new_score_map = {"A": 1, "B": 2, "C": 3}
tactic_map = {"X": 0, "Y": 3, "Z": 6}


def get_loss(inp):
    return new_score_map[loss_map[inp]]


def get_win(inp):
    return new_score_map[win_map[inp]]


total = 0
for opponent, you in lines:

    total += tactic_map[you]

    if you == "X":
        total += get_loss(opponent)
    elif you == "Y":
        total += new_score_map[opponent]
    else:
        total += get_win(opponent)


print(total)
