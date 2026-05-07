class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        for i in range(rows):
            if matrix[i][cols-1] < target:
                continue
            l, r = 0, cols-1
            while l <= r:
                mid = l+(r-l)//2
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] < target:
                    l = mid+1
                else:
                    r = mid-1
        return False
            