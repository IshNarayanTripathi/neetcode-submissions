# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        def check(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            return p.val == q.val and check(p.left, q.left) and check(p.right, q.right)
        def dfs(node):
            if not node:
                return False
            if check(node, subroot):
                return True
            left = dfs(node.left)
            right = dfs(node.right)
            return left or right
        return dfs(root)

            
            

