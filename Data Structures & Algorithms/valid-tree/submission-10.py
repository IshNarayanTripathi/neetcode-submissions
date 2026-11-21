class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent = list(range(n))
        rank = [0]*n
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
        for u, v in edges:
            if union(u, v):
                return False
        for i in range(n):
            find(i)
        return len(set(parent)) == 1
