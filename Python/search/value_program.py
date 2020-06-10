# ----------
# User Instructions:
#
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal.
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------
from pprint import pprint

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0]]
goal = [len(grid) - 1, len(grid[0]) - 1]
cost = 1  # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']


def compute_value(grid, goal, cost):
    # ----------------------------------------
    # insert code below
    # ----------------------------------------
    value = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]

    searched = set()

    open = {(0, goal[0], goal[1]), }

    while len(open) > 0:
        prev_value = min(open, key=lambda x: x[0])
        open.remove(prev_value)
        c, x, y = prev_value
        searched.add((x, y))
        value[x][y] = c

        for (d_x, d_y) in delta:
            x_n = x + d_x
            y_n = y + d_y

            if (x_n, y_n) not in searched and 0 <= x_n < len(grid) and 0 <= y_n < len(grid[0]) and grid[x_n][
                y_n] == 0:
                c2 = c + cost
                open.add((c2, x_n, y_n))

    # make sure your function returns a grid of values as
    # demonstrated in the previous video.
    return value


value = compute_value(grid, goal, cost)
pprint(value)
