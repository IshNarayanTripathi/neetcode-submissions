class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        visited = set()
        def bfs(node):    
            
            queue = deque([node])
            while queue:
                node = queue.popleft()
                visited.add(node)
                for nei in adj_list[node]:
                    if nei not in visited:
                        
                        queue.append(nei)
                        visited.add(nei)
           
        bfs(0)
        return len(visited) == n



