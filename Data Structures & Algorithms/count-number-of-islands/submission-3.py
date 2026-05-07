class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        def bfs(i, j):
            queue = deque([(i, j)])
            visited.add((i, j))
            while queue:
                r, c = queue.popleft()
                for x, y in directions:
                    nr, nc = r+x, c+y
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] == "1":
                        visited.add((nr, nc))
                        queue.append((nr, nc))
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    count += 1
                    bfs(i, j)
        return count