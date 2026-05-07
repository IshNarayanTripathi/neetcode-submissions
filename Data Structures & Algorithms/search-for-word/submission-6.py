class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        def bfs(r, c, visited, index):
            queue = deque([(r, c, visited, index)])
            while queue:
                r,c, visited, index = queue.popleft()
                if index == len(word):
                    return True
                visited.add((r, c))
                for x, y in directions:
                    nr, nc = r+x, c+y
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and board[nr][nc] == word[index]:
                        queue.append((nr, nc, visited | {(nr, nc)}, index+1))
            return False
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if bfs(i, j, set(), 1):
                        return True
        return False

