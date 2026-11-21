class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n+1))
        rank = [0]*(n+1)
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            rootx = find(x)
            rooty = find(y)
            if rootx == rooty:
                return True
            if rank[rootx] > rank[rooty]:
                parent[rooty] = rootx
                rank[rootx] += 1
            elif rank[rootx] < rank[rooty]:
                parent[rootx] = rooty
                rank[rooty] += 1
            else:
                parent[rooty] = rootx
                rank[rootx] += 1
            return False
        s = r = float("inf")
        for u, v in edges:
            if union(u, v):
                s, r = u, v
        return [s, r]
        