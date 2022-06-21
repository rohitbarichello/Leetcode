def dfs(grid, i, j):
    if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == "1":
        grid[i][j] = "0"

        dfs(grid, i + 1, j)
        dfs(grid, i - 1, j)
        dfs(grid, i, j + 1)
        dfs(grid, i, j - 1)


def numIslands(grid) -> int:
    if not grid:
        return 0

    islands = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                dfs(grid, i, j)
                islands += 1

    return islands


# lessons learned
# 1. if I'm running demorgans law on a conditional statement I need to make sure to
# reverse the and to an or and vice versa
# 2. i need to remember the difference between incluseive <> and exclusive expresssions
# 3. I need to be able to say what my algorithm is doing in plain terms. in this case my algorithm
# is identifying an island then sinking it so it can't be discovered again. I do this for every cell until i find
# my stuff
