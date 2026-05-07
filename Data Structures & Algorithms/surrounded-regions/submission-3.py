from collections import deque
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        rows, cols = len(board), len(board[0])

        def bfs(starts):
            queue = deque(starts)
            visited = set(starts)  
            while queue:
                r, c = queue.popleft()
                board[r][c] = -1
                for x, y in [(1,0),(0,1),(-1,0),(0,-1)]:
                    nr, nc = r+x, c+y
                    if (0 <= nr < rows and 0 <= nc < cols and 
                        (nr, nc) not in visited and board[nr][nc] == 'O'):
                        queue.append((nr, nc))
                        visited.add((nr, nc))

        # collect border 'O's
        topleft = [(r, 0) for r in range(rows) if board[r][0] == 'O'] \
                + [(0, c) for c in range(cols) if board[0][c] == 'O']
        bottomright = [(r, cols-1) for r in range(rows) if board[r][cols-1] == 'O'] \
                + [(rows-1, c) for c in range(cols) if board[rows-1][c] == 'O']

        bfs(topleft)
        bfs(bottomright)

      
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == -1:
                    board[i][j] = 'O'
