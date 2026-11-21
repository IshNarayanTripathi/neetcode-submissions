"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        oldToNew = {None:None}
        visited = set()
        curr = node
        def dfs(x):
            new_node = Node(x.val)
            visited.add(x)
            oldToNew[x] = new_node
            for neighbor in x.neighbors:
                if neighbor not in visited:
                    dfs(neighbor)
        dfs(curr)
        visited.clear()
        curr = node
        def dfs2(x):
            new_node = oldToNew[x]
            visited.add(x)
            for neighbor in x.neighbors:
                new_node.neighbors.append(oldToNew[neighbor])
                if neighbor not in visited:
                    dfs2(neighbor)
        dfs2(curr)
        return oldToNew[node]
            