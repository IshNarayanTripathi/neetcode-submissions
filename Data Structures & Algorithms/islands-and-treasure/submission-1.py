class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        #visited = set()
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append((i, j))
        while queue:
            r, c = queue.popleft()
            #visited.add((r, c))
            for x, y in directions:
                nr, nc = r+x, c+y
                if 0<=nr<rows and 0<=nc<cols  and grid[nr][nc] == 2147483647 :
                    grid[nr][nc] = 1 + grid[r][c]
                    queue.append((nr, nc))