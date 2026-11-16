class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        total = 0
        directions = [(1,0), (0,1)]
        dp = {}
        def traverse(i, j, visited):
            nonlocal total
            if i == m-1 and j == n-1:
                # total += 1
                return 1
            if i >= m or j >= n:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            res = 0
            for x, y in directions:
                nr, nc = i+x, j+y
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                    res += traverse(nr, nc, visited | {nr, nc})
            dp[(i, j)] = res
            return dp[(i, j)]
        return traverse(0, 0, set())
        # return total
            
