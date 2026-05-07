class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = {i:i for i in range(1, n+1)}
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            rootx = find(x)
            rooty = find(y)
            if rootx == rooty:
                return False
            parent[rooty] = rootx
            return True
        for u, v in edges:
            if not union(u, v):
                return [u, v]
            