class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        last_x, last_y = 0, 0
        parent = [i for i in range(len(edges)+1)]
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x,y):
            parent_x = find(x)
            parent_y = find(y)
            parent[parent_y] = parent_x
        for u,v in edges:
            if find(u) == find(v):
                last_x, last_y = u, v
            union(u,v)
        return [last_x, last_y]