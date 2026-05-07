class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows, cols = m, n
        directions = [(1,0), (0,1)]
        queue = deque([(0,0, set((0, 0)))])
        paths = 0
        while queue:
            r, c, visited = queue.popleft()
            if r == rows-1 and c == cols-1:
                paths += 1
            for x, y in directions:
                nr, nc = r+x, c+y
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    queue.append((nr, nc, visited | {nr, nc}))
        return paths

