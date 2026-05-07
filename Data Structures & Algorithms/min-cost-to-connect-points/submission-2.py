class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                dist = abs(x1-x2)+abs(y1-y2)
                adj_list[i].append((dist,j))
                adj_list[j].append((dist,i))
        min_heap = [(0,0)]
        visited = [False]*len(points)
        res = 0
        while min_heap:
            cost, node = heapq.heappop(min_heap)
            if visited[node]:
                continue
            visited[node] = True                
            res += cost
            for neic, nei in adj_list[node]:
                if not visited[nei]:
                    heapq.heappush(min_heap,(neic, nei))
        return res