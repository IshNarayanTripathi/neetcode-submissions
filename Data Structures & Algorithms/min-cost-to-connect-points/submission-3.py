class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = defaultdict(list)
        res = 0
        visited = [False]*len(points)
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                dist = abs(x1-x2)+abs(y1-y2)
                graph[i].append((dist, j))
                graph[j].append((dist, i))
        min_heap = [(0, 0)]
        while min_heap:
            cost, node = heapq.heappop(min_heap)
            
            if visited[node]:
                continue
            visited[node] = True
            res += cost
            for neic, nei in graph[node]:
                if not visited[nei]:
                    heapq.heappush(min_heap, (neic, nei))
        return res