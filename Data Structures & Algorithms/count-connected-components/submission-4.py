class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        def find(x):
            if parent[x]  != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            rootx = find(x)
            rooty = find(y)
            if rootx != rooty:
                parent[rooty] = rootx
        for u, v in edges:
            union(u, v)
        return len(set(find(i) for  i in range(n)))