class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (0, 1), (-1, 0), (0, -1)]
        max_area = 0
        visited = set()
        def dfs(i, j, curr):
            nonlocal max_area
            visited.add((i, j))
            for x, y in directions:
                nr, nc = x+i, y+j
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] == 1:
                    dfs(nr, nc, curr+1)
            max_area = max(max_area, curr)
        prev_len = 0
        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visited and grid[i][j] == 1:
                    dfs(i, j, 1)
                max_area = max(max_area, len(visited)-prev_len)
                prev_len = len(visited)
        return max_area