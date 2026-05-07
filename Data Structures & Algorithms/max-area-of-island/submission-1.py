class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_area = float("-inf")
        visited = set()
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        def bfs(r, c):
            queue = deque([(r, c)])
            visited.add((r, c))
            area = 1
            while queue:
                r, c = queue.popleft()
                for x, y in directions:
                    nr, nc = r+x, c+y
                    if 0<=nr<rows and 0<=nc<cols and (nr, nc) not in visited and grid[nr][nc] == 1:
                        queue.append((nr, nc))
                        visited.add((nr, nc))
                        area+=1
            return area
        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visited and grid[i][j] == 1:
                    max_area = max(max_area, bfs(i, j))
        return max_area if max_area != float("-inf") else 0