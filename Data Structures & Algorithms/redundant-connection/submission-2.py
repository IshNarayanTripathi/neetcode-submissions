class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n+1)]
        def find(x):
            if parent[x] !=  x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(u, v):
            parent_v = find(v)
            parent_u = find(u)
            parent[parent_v] = parent_u
        res = []
        for u, v in edges:
            if find(u) == find(v):
                res.append([u, v])
            union(u, v)
        return res[-1]
