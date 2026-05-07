class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent = {i:i for i in range(n)}
        def find(x):
            if parent[x] !=  x:
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
                return False
        return True and len(edges) == n - 1
        # visited = set()
        # graph = defaultdict(list)
        # for u, v  in edges:
        #     graph[u].append(v)
        # def dfs(node):
        #     if node in visited:
        #         return False
        #     visited.add(node)
        #     for nei in graph[node]:
        #         dfs(nei)
        #     return True
        # return dfs(0)