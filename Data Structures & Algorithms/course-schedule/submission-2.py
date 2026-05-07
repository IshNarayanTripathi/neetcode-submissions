class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        indegree = defaultdict(int)
        res = []
        for u, v in prerequisites:
            adj[v].append(u)
            indegree[u] += 1
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        while queue:
            node = queue.popleft()
            res.append(node)
            for nei in adj[node]:
                indegree[nei] -= 1
                if not indegree[nei]:
                    queue.append(nei)
        return len(res) == numCourses