class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        distance = [float("inf")]*(n+1)
        distance[k] = 0
        for i in range(n-1):
            for u,v,w in times:
                if distance[u] != float("inf") and distance[v] > distance[u]+w:
                    distance[v] = distance[u]+w
        for u,v,w in times:
                if distance[u] != float("inf") and distance[v] > distance[u]+w:
                    return -1
        res = max(distance[1:])
        return res if res != float("inf") else -1
        

