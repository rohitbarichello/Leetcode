def dfs(matrix, i, j, points, visited):
    if (i, j) not in visited:
        points.add((i, j))
        visited.add((i, j))

        # up
        if i - 1 >= 0 and matrix[i - 1][j] >= matrix[i][j]:
            dfs(matrix, i - 1, j, points, visited)

        # down
        if i + 1 < len(matrix) and matrix[i + 1][j] >= matrix[i][j]:
            dfs(matrix, i + 1, j, points, visited)

        # left
        if j - 1 >= 0 and matrix[i][j - 1] >= matrix[i][j]:
            dfs(matrix, i, j - 1, points, visited)

        # right
        if j + 1 < len(matrix[0]) and matrix[i][j + 1] >= matrix[i][j]:
            dfs(matrix, i, j + 1, points, visited)

    return


class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if matrix:
            pacific_visited = set()
            atlantic_visited = set()
            pacific_highest_points = set()
            atlantic_highest_points = set()

            # left and right side
            for i in range(len(matrix)):
                dfs(matrix, i, 0, pacific_highest_points, pacific_visited)
                dfs(
                    matrix,
                    i,
                    len(matrix[0]) - 1,
                    atlantic_highest_points,
                    atlantic_visited,
                )

            # top and bottom
            for j in range(len(matrix[0])):
                dfs(matrix, 0, j, pacific_highest_points, pacific_visited)
                dfs(
                    matrix,
                    len(matrix) - 1,
                    j,
                    atlantic_highest_points,
                    atlantic_visited,
                )

            return list(pacific_highest_points & atlantic_highest_points)
        else:
            return []
