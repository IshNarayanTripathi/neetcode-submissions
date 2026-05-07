class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        def bfs(r, c):
            queue = deque([(r, c)])
            visited.add((r, c))
            while queue:
                r, c = queue.popleft()
                for x, y in directions:
                    nr, nc = r+x, c+y 
                    if 0 <= nr < rows and 0 <= nc < cols and(nr, nc) not in visited and grid[nr][nc] == "1":
                        queue.append((nr, nc))
                        visited.add((nr, nc))
        count = 0
        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visited and grid[i][j] == "1":
                    bfs(i, j)
                    count += 1
        return count