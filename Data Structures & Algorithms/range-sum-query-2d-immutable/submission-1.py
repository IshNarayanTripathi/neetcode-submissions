class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.NumMatrix = [[0]*(cols+1) for _ in range(rows+1)]
        for i in range(rows):
            prefix = 0
            for j in range(cols):
                prefix += matrix[i][j]
                above = self.NumMatrix[i][j+1]
                self.NumMatrix[i+1][j+1] = prefix+above

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        bottomRight = self.NumMatrix[r2+1][c2+1]
        above = self.NumMatrix[r1][c2+1]
        left = self.NumMatrix[r2+1][c1]
        topleft = self.NumMatrix[r1][c1]
        return bottomRight-above-left+topleft


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)