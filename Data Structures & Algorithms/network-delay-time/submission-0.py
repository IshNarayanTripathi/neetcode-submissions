class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        distance = [float('inf')]*(n+1)
        for u,v,w in times:
            graph[u].append((v,w))
        distance[k] = 0
        distance[0] = 0
        min_heap = [(0, k)]
        while min_heap:
            d, n = heapq.heappop(min_heap)
            if d == float('inf'):
                continue
            for v,w in graph[n]:
                if distance[v] > d+w:
                    distance[v] = d+w
                    heapq.heappush(min_heap, (w+d,v))
        max_dist = max(distance)
        return max_dist if max_dist != float('inf') not in distance else -1