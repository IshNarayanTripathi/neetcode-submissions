class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj_list = defaultdict(list)
        for u, v in prerequisites:
            adj_list[u].append(v)
        
        def dfs(u, v, visited):
            if u == v:
                return True
          
            for nei in adj_list[u]:
                if nei not in visited:
                    visited.add(nei)
                    if dfs(nei, v, visited):
                        return True
            return False
        res = []
        for u, v in queries:
            res.append(dfs(u, v, set()))
        return res