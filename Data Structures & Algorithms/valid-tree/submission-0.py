class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False  # not fully connected

        parent = [i for i in range(n)]
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            parent_x = find(x)
            parent_y = find(y)
            parent[parent_y] = parent_x
        for x, y in edges:
            if find(x) == find(y):
                return False
            union(x,y)
        return True