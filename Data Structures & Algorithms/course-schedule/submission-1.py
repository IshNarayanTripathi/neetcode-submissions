class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for u, v in prerequisites:
            graph[v].append(u)
            indegree[u]+=1
        topo = []
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        while queue:
            node = queue.popleft()
            topo.append(node)
            for nei in graph[node]:
                indegree[nei]-=1
                if indegree[nei] == 0:
                    queue.append(nei)
        return len(topo) == numCourses