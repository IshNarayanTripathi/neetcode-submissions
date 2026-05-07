class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        coord = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    coord.append((i, j))
        for x, y in coord:
            for j in range(len(matrix[0])):
                matrix[x][j]= 0
            for i in range(len(matrix)):
                matrix[i][y] = 0
        