class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float("inf")]*(n+1)
        dist[k] = 0
        for i in range(n-1):
            for u,v,w in times:
                if dist[u]+w < dist[v]:
                    dist[v] = dist[u]+w
        
        max_val = max(dist[1:]) 
        return max_val if max_val != float("inf") else -1