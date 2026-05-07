class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        for i in range(rows):
            if target > matrix[i][cols-1]:
                continue
            left, right = 0, cols-1
            while left <=  right:
                mid = left+(right-left)//2
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] > target:
                    right = mid-1
                else:
                    left = mid+1
        return False
