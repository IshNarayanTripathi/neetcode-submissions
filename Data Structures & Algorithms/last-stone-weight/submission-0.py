import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-num for num in stones]
        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            s1 = heapq.heappop(max_heap)
            s2 = heapq.heappop(max_heap)
            diff = abs(abs(s1)-abs(s2))
            if diff > 0:
                heapq.heappush(max_heap, -diff)
        return abs(max_heap[0]) if max_heap else 0