class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        def bfs(i, j):
            queue = deque([(i, j)])
            
            while queue:
                r, c = queue.popleft()
                board[r][c] = 1
                for x, y in directions:
                    nr, nc = r+x, c+y
                    if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O":
                        board[nr][nc] = 1
                        queue.append((nr, nc))
        for i in range(rows):
            if board[i][0] == "O":
                bfs(i, 0)
            if board[i][cols-1] == "O":
                bfs(i, cols-1)
        for i in range(cols):
            if board[0][i] == "O":
                bfs(0, i)
            if board[rows-1][i] == "O":
                bfs(rows-1, i)
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 1:
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
                
         

