class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj_list = defaultdict(list)
        for u,v in prerequisites:
            adj_list[v].append(u)
        
        def dfs(node, target, visited):
            if node == target:
                return True
            for child in adj_list[target]:
                if child not in visited:
                    visited.add(child)
                    if dfs(node, child, visited):
                        return True
            return False
        res = []
        for u, v in queries:
            res.append(dfs(u, v, set()))
        return res


