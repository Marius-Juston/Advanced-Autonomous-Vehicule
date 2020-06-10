# ----------
# User Instructions:
#
# Write a function optimum_policy that returns
# a grid which shows the optimum policy for robot
# motion. This means there should be an optimum
# direction associated with each navigable cell from
# which the goal can be reached.
#
# Unnavigable cells as well as cells from which
# the goal cannot be reached should have a string
# containing a single space (' '), as shown in the
# previous video. The goal cell should have '*'.
# ----------
from pprint import pprint

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid) - 1, len(grid[0]) - 1]
cost = 1  # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['v', '>', '^', '<']


def optimum_policy(grid, goal, cost):
    # ----------------------------------------
    # insert code below
    # ----------------------------------------
    policy = [[' ' for _ in range(len(grid[0]))] for _ in range(len(grid))]
    value = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]

    searched = set()

    open = {(0, goal[0], goal[1]), }
    policy[goal[0]][goal[1]] = '*'

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

                position = (1 + d_x) * (d_x != 0) + (2 + d_y) * (d_y != 0)
                print(d_x, d_y, position)

                policy[x_n][y_n] = delta_name[position]

    # make sure your function returns a grid of values as
    # demonstrated in the previous video.
    return policy, value


path, v = optimum_policy(grid, goal, cost)
pprint(v)
pprint(path)
