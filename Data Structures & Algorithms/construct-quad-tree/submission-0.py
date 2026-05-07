"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        return self.build(grid, 0, 0, len(grid))

    def build(self, grid, row, col, size):
        if self.isUniform(grid, row, col, size):
            return Node(val = bool(grid[row][col]), isLeaf = True)
        half = size//2
        topleft = self.build(grid, row, col, half)
        topright = self.build(grid, row, col+half, half)
        bottomleft = self.build(grid, row+half, col, half)
        bottomright = self.build(grid, row+half, col+half, half)
        return Node(val = True,
        isLeaf = False,
        topLeft = topleft,
        topRight = topright,
        bottomLeft = bottomleft,
        bottomRight = bottomright)

    def isUniform(self, grid, row, col, size):
        val = grid[row][col]
        for i in range(row, row+size):
            for j in range(col, col+size):
                if grid[i][j] != val:
                    return False
        return True