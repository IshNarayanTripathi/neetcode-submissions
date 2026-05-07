class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_area = 0
        visited = set()
        def bfs(i, j):
            area = 1
            queue = deque([(i,j)])
            
            directions = [(1,0),(0,1),(-1,0),(0,-1)]
            while queue:
                r,c= queue.popleft()
                visited.add((r, c))
                for x,y in directions:
                    nr, nc = r+x, c+y
                    if 0<=nr<rows and 0<=nc<cols and (nr, nc) not in visited and grid[nr][nc] == 1:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
                        area+=1
            return area
        for i in range(rows):
            for j in range(cols):
                if (i,j) not in visited and grid[i][j] == 1:
                    area = bfs(i, j)
                    max_area = max(max_area, area)
        return max_area
