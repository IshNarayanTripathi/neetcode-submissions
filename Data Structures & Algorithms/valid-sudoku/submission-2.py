class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r_v = [set() for _ in range(9)]
        c_v = [set() for _ in range(9)]
        g_v = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                if val in r_v[i]:
                    return False
                if val in c_v[j]:
                    return False
                key = (i//3)*3+(j//3)
                if val in g_v[key]:
                    return False
                r_v[i].add(val)
                c_v[j].add(val)
                g_v[key].add(val)
        return True