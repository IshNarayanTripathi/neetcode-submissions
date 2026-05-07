class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(u, v):
            parent_v = find(v)
            parent_u = find(u)
            if parent_v != parent_u:
                parent[parent_v] = parent_u
        count = 0
        for u, v in edges:
            if find(u) != find(v):
                union(u, v)
                count += 1
        return len(set(find(i) for  i in range(n)))