# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        total = 0
        def traverse(node, max_val):
            nonlocal total
            if not node:
                return
            if node.val >= max_val:
                total+=1
                max_val = node.val
            traverse(node.left, max_val)
            traverse(node.right, max_val)
            
        traverse(root, float("-inf"))
        return total