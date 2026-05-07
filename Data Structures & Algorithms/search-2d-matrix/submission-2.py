class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        for i in range(rows):
            if target > matrix[i][cols-1]:
                continue
            for j in range(cols):
                if matrix[i][j] == target:
                    return True
        return False