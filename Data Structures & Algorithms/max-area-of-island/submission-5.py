class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (0, 1), (-1, 0), (0, -1)]
        visited = set()
        def bfs(i, j):
            queue = deque([(i, j, 1)])
            visited.add((i, j))
            #curr_area = float("-inf")
            curr_area = 1
            while queue:
                r, c, a = queue.popleft()
                #curr_area = max(curr_area, a)
                
                for x, y in directions:
                    nr, nc = r+x, c+y
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] == 1:
                        visited.add((nr, nc))
                        queue.append((nr, nc, a+1))
                        curr_area += 1
            return curr_area
        max_area = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visited:
                    max_area = max(max_area, bfs(i, j))
        return max_area 