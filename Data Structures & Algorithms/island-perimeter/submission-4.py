class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def bfs(i, j):
            perimeter =  0
            queue = deque([(i, j)])
            visited.add((i, j))
            while queue:
                r, c = queue.popleft()
                for x, y in directions:
                    nr, nc = r+x, c+y
                    if not (0 <= nr < rows and 0 <= nc < cols) or grid[nr][nc] == 0:
                        perimeter += 1
                    elif (nr, nc) not in visited:
                        queue.append((nr, nc))
                        visited.add((nr, nc))
            return perimeter
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return bfs(i, j)