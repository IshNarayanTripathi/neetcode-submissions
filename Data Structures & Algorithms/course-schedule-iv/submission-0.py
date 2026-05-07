class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)
        def dfs(u, v):
            if v in graph[u]:
                return True
            for nei in graph[u]:
                return dfs(nei, v)
            return False
        result = []
        for u,v in queries:
            if u not in graph:
                result.append(False)
                continue
            if dfs(u, v):
                result.append(True)
            else:
                result.append(False)
        return result
        