class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        def bfs(r, c):
            visited = set()
            queue = deque([(r, c)])
            isPacific = False
            isAtlantic = False
            while queue:
                r, c = queue.popleft()
                visited.add((r, c))
                val = heights[r][c]
                if r == 0 or c == 0:
                    isPacific = True
                if r == rows-1 or c == cols-1:
                    isAtlantic = True
                if isPacific and isAtlantic:
                    return True
                for x,y in directions:
                    nr, nc = r+x, c+y
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and heights[nr][nc] <= val:
                        queue.append((nr, nc))
                        visited.add((nr, nc))
            return isPacific and isAtlantic
        result = []
        for i in range(rows):
            for j in range(cols):
                if bfs(i, j):
                    result.append((i, j))
        return result