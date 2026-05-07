class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.sum_mat = [[0]*(cols+1) for _ in range(rows+1)]
        for i in range(rows):
            prefix = 0
            for j in range(cols):
                prefix += matrix[i][j]
                self.sum_mat[i+1][j+1] = prefix+self.sum_mat[i][j+1]

   

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 += 1
        col1 += 1
        row2 += 1
        col2 += 1
        bottomleft = self.sum_mat[row2][col2]
        bottomright = self.sum_mat[row2][col1-1]
        topleft = self.sum_mat[row1-1][col1-1]
        topright = self.sum_mat[row1-1][col2]
        return bottomleft-bottomright-topright+topleft