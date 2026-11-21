class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = [(1,0), (0,1), (-1,0), (0, -1)]
        def dfs(i, j):
            
            visited.add((i, j))
            for x, y in directions:
                nr, nc = i+x, j+y
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[i][j] == "1":
                    dfs(nr, nc)
        count = 0
        for i in range(rows):
            for j in range(cols):
                if (i, j)  not in visited and grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        return count