class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        max_area = 0
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        def bfs(r, c):
            area = 0
            queue = deque([(r, c)])
            while queue:
                r, c = queue.popleft()
                visited.add((r, c))
                area += 1
                for x, y in directions:
                    nr, nc = r+x, c+y
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] == 1:
                        queue.append((nr, nc))
                        visited.add((nr, nc))
            return area
        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visited and grid[i][j] == 1:
                    max_area = max(max_area, bfs(i, j))
        return max_area 

