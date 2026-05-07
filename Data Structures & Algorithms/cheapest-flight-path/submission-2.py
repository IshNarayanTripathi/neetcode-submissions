class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [float("inf")]*n
        dist[src] = 0
        for i in range(k+1):
            temp = dist.copy()
            for u,v,w in flights:
                if dist[u] != float("inf") and temp[v] > dist[u]+w:
                    temp[v] = dist[u]+w
            dist = temp
        val = dist[dst]
        return val if val != float("inf") else -1