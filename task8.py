with open("input8.txt") as f:
    lines = [l.strip() for l in f.readlines()]

len_rows = len(lines[0])
len_cols = len(lines)
# outside edge is always visible
visible = 0
vis_factor = float("-Inf")


def search_directions(start, end, num, default_row=None, default_col=None):
    global visible

    visibility = True
    # top
    for i in range(start, end):
        if (
            lines[default_row if default_row else i][default_col if default_col else i]
            >= num
            and visibility
        ):
            visibility = False
            break

    if visibility:
        visible += 1
        return True

    return False


def search(row, col, num):
    global vis_factor

    factor1, factor2, factor3, factor4 = [0] * 4

    if row - 1 == 0:
        factor1 = 1
    for i in range(row - 1, 0, -1):
        if lines[i][col] < num:
            factor1 += 1
        else:
            factor1 += 1
            break

    if row + 1 == len_rows - 1:
        factor2 = 1
    for i in range(row + 1, len_rows):
        if lines[i][col] < num:
            factor2 += 1
        else:
            factor2 += 1
            break

    if col - 1 == 0:
        factor3 = 1
    for i in range(col - 1, 0, -1):
        if lines[row][i] < num:
            factor3 += 1
        else:
            factor3 += 1
            break

    if col + 1 == len_cols - 1:
        factor4 = 1
    for i in range(col + 1, len_cols):
        if lines[row][i] < num:
            factor4 += 1
        else:
            factor4 += 1
            break

    product = factor1 * factor2 * factor3 * factor4

    print(factor1, factor2, factor3, factor4, num)

    vis_factor = max(product, vis_factor)

    # top
    if search_directions(0, row, num, default_col=col):
        return

    # bottom
    if search_directions(row + 1, len_rows, num, default_col=col):
        return

    # left
    if search_directions(0, col, num, default_row=row):
        return

    # right
    if search_directions(col + 1, len_cols, num, default_row=row):
        return


for i in range(len_rows):
    for j in range(len_cols):
        if i == 0 or j == 0 or i == len_rows - 1 or j == len_cols - 1:
            visible += 1
            continue

        search(i, j, lines[i][j])

print(visible, vis_factor)
