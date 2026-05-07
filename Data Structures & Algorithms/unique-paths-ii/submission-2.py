class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return 0
        rows, cols = len(grid), len(grid[0])
        dp = [[0]*cols for _ in range(rows)]
        dp[0][0] = 1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    dp[r][c] = 0
                    continue
                if r > 0:
                    dp[r][c] += dp[r-1][c]
                if c > 0:
                    dp[r][c] += dp[r][c-1]
        return dp[rows-1][cols-1]