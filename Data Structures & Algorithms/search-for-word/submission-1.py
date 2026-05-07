class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        queue = deque()
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        for i in range(rows):
            for j in range(cols):
                if  board[i][j] == word[0]:
                    queue.append((i, j, 1,{(i,j)}))
        
        
                    while queue:
                        r, c, ind, visited = queue.popleft()
                        
                        if ind == len(word):
                            return True
                        for x,y in directions:
                            nr, nc = r+x, c+y
                            if 0<=nr<rows and 0<=nc<cols and (nr, nc) not in visited and board[nr][nc] == word[ind]:
                                
                                queue.append((nr,nc,ind+1, visited | {(nr,nc)}))
        return False
            
