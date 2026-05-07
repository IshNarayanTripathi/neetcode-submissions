class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            parent[find(y)] = find(x)
        for u,v in edges:
            union(u, v)
        for i in range(n):
            find(i)
        
        return len(set(parent))