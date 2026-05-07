class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows, cols = m, n
        count = 0
        queue = deque([(0,0)])
        directions = [(1,0),(0,1)]
        while queue:
            r,c = queue.popleft()
            
            if r == rows-1 and c == cols-1:
                count += 1
            for x,y in directions:
                nr, nc = r+x, c+y 
                if 0 <= nr < rows and 0 <= nc < cols:
                    queue.append((nr, nc))
        return count