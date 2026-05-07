class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        count = 0
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        def bfs(i, j):
            queue = deque([(i,j)])
            while queue:
                r, c = queue.popleft()
                visited.add((r, c))
                for x,y in directions:
                    nr, nc = r+x, c+y
                    if 0<=nr<rows and 0<=nc<cols and (nr, nc) not in visited and grid[nr][nc] == "1":
                        visited.add((nr, nc))
                        queue.append((nr, nc))
        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visited and grid[i][j] == "1":
                    bfs(i, j)
                    count += 1
        return count


