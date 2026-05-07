class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _  in range(9)]
        cols = [set() for _ in range(9)]
        grid = [set() for _ in range(9)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                val = board[i][j]
                if val in rows[i]:
                    return False
                if val in cols[j]:
                    return False
                grid_id = (i//3)*3+j//3
                if val in grid[grid_id]:
                    return False
                rows[i].add(val)
                cols[j].add(val)
                grid[grid_id].add(val)
        return True