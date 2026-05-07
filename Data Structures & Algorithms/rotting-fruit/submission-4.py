class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        visited = set()
        timer = 0
        while queue:
            size = len(queue)
            changed = False
            for _ in range(size):
                r, c = queue.popleft()
                visited.add((r, c))
                for x, y in directions:
                    nr, nc = r+x, c+y
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc)  not in visited and grid[nr][nc] == 1:
                        changed = True
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                        visited.add((nr, nc))
                        fresh -= 1
            if changed:
                timer += 1
        return timer if not fresh else -1








            