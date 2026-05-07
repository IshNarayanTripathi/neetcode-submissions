from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        indegree = defaultdict(int)
        graph = defaultdict(list)
        for u,v in prerequisites:
            graph[v].append(u)
            indegree[u]+=1
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        topo = []
        while queue:
            node = queue.popleft()
            topo.append(node)
            for neighbor in graph[node]:
                indegree[neighbor]-=1
                if not indegree[neighbor]:
                    queue.append(neighbor)
        return len(topo) == numCourses