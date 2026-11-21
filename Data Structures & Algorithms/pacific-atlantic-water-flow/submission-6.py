class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        res = []
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def bfs(i, j):
            isAtlantic = isPacific = False
            queue = deque([(i, j)])
            visited = set()
            while queue:
                r, c = queue.popleft()
                visited.add((r, c))
                if r == 0 or c == 0:
                    isPacific = True
                if r == rows-1 or c == cols-1:
                    isAtlantic = True
                if isAtlantic and isPacific:
                    return True
                val = heights[r][c]
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and heights[nr][nc] <= val:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            return False
        for i in range(rows):
            for j in range(cols):
                if bfs(i, j):
                    res.append([i, j])
        return res