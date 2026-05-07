class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        
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
        return topo if len(topo) == numCourses else []