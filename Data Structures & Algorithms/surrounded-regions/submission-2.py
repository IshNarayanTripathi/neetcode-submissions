class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        queue = deque()
        for i in range(rows):
            for j in [0, cols-1]:
                if board[i][j] == "O":
                    queue.append((i, j))
        for j in range(cols):
            for i in [0, rows-1]:
                if board[i][j] == "O":
                    queue.append((i, j))
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        while queue:
            r, c = queue.popleft()
            board[r][c] = "T"
            for x,y in directions:
                nr = r+x
                nc = c+y
                if 0<= nr< rows and 0 <= nc < cols and board[nr][nc] == "O":
                    queue.append((nr, nc))

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"
        