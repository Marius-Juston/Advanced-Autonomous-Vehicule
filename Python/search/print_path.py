# -----------
# User Instructions:
#
# Modify the the search function so that it returns
# a shortest path as follows:
#
# [['>', 'v', ' ', ' ', ' ', ' '],
#  [' ', '>', '>', '>', '>', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', '*']]
#
# Where '>', '<', '^', and 'v' refer to right, left,
# up, and down motions. Note that the 'v' should be
# lowercase. '*' should mark the goal cell.
#
# You may assume that all test cases for this function
# will have a path from init to goal.
# ----------
from pprint import pprint

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]
init = [0, 0]
goal = [len(grid) - 1, len(grid[0]) - 1]
cost = 1

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['<', 'v', '>', '^']


def search(grid, init, goal, cost):
    # ----------------------------------------
    # modify code below
    # ----------------------------------------
    expand = [[' ' for _ in range(len(grid[0]))] for _ in range(len(grid))]

    index = 0
    searched = {tuple(init): None}
    open = {(0, init[0], init[1]), }

    while len(open) > 0:
        cell = min(open, key=lambda x: x[0])
        open.remove(cell)
        g, x, y = cell
        index += 1

        for (d_x, d_y) in delta:
            x_n = x + d_x
            y_n = y + d_y

            if (x_n, y_n) not in searched and 0 <= x_n < len(grid) and 0 <= y_n < len(grid[0]) and grid[x_n][
                y_n] == 0:
                path = (g + cost, x_n, y_n)
                open.add(path)
                searched[(x_n, y_n)] = (x, y)

                if x_n == goal[0] and y_n == goal[1]:
                    expand[x_n][y_n] = '*'

                    previous = (x_n, y_n)
                    while not previous == tuple(init):
                        next_point = searched[previous]

                        index_x = (previous[0] - next_point[0])
                        index_y = (previous[1] - next_point[1])

                        if index_x > 0:
                            expand[next_point[0]][next_point[1]] = 'v'
                        elif index_x < 0:
                            expand[next_point[0]][next_point[1]] = '^'
                        elif index_y < 0:
                            expand[next_point[0]][next_point[1]] = '<'
                        else:
                            expand[next_point[0]][next_point[1]] = '>'

                        previous = next_point

                    return expand

    return expand


path = search(grid, init, goal, cost)

pprint(path)
