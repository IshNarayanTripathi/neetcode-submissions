class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [[0]*cols for _ in range(rows)]
        dp[0][0] = grid[0][0]
        for r in range(rows):
            for c in range(cols):
                if r == 0 and c == 0:
                    continue
                min_above = min_left = float("inf") 
                if r > 0:
                    min_above = dp[r-1][c]
                if c > 0:
                    min_left = dp[r][c-1]
                dp[r][c] += grid[r][c]+min(min_above, min_left)       
        return dp[rows-1][cols-1]
        