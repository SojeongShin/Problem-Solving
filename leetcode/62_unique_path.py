class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0] * n for _ in range(m)]

        if m == 1 and n==1:
            grid[0][0] = 1

        elif m == 1:
            grid[0][1] = 1
            for j in range(2, n):
                grid[0][j] = grid[0][j-1]


        for i in range(1, m):
            grid[i][0] = 1
            for j in range(1, n):
                grid[0][j] = 1
                grid[i][j] = grid[i-1][j] + grid[i][j-1]

        return grid[m-1][n-1]
        