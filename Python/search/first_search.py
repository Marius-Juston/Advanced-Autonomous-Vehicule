# ----------
# User Instructions:
#
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space


grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid) - 1, len(grid[0]) - 1]
cost = 1

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']


def search(grid, init, goal, cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------

    searched = dict()
    open = {(0, init[0], init[1]), }

    while len(open) > 0:
        cell = min(open, key=lambda x: x[0])
        open.remove(cell)
        g, x, y = cell

        for (d_x, d_y) in delta:
            x_n = x + d_x
            y_n = y + d_y

            if (x_n, y_n) not in searched and 0 <= x_n < len(grid) and 0 <= y_n < len(grid[0]) and grid[x_n][y_n] == 0:
                path = (g + cost, x_n, y_n)
                open.add(path)
                searched[(x_n, y_n)] = (x, y)

                if x_n == goal[0] and y_n == goal[1]:
                    return g + cost, x_n, y_n

    return 'fail'


path = search(grid, init, goal, cost)
print(path)
