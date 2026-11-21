from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: list[list[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        queue = deque()

        # Add all treasure cells as starting points
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append((i, j))

        # Multi-source BFS
        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (0 <= nr < rows and
                    0 <= nc < cols and
                    grid[nr][nc] == 2147483647):

                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr, nc))