class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        atlantic = [[False]*cols for _ in range(rows)]
        pacific = [[False]*cols for _ in range(rows)]
        res = []
        def bfs(r, c):
            visited = set()
            directions = [(1,0),(0,1),(-1,0),(0,-1)]
            queue = deque([(r, c)])
            pacific = False
            atlantic = False
            
            while queue:
                r, c = queue.popleft()
                visited.add((r, c))
                if c == 0 or  r == 0:
                    pacific = True
                if c == cols-1 or r == rows-1:
                    atlantic = True
                for x,y in directions:
                    nr, nc = r+x, c+y
                    if 0<=nr<rows and 0<=nc<cols and (nr,nc) not in visited and heights[nr][nc] <= heights[r][c]:
                        queue.append((nr, nc))
            return atlantic and pacific
        for i in range(rows):
            for j in range(cols):
                if bfs(i, j):
                    res.append((i, j))
        return res
