class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-i for i in stones]
        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            first = heapq.heappop(max_heap)*-1
            second = heapq.heappop(max_heap)*-1
            diff = abs(first-second)
            if diff > 0:
                heapq.heappush(max_heap, -diff)
        return max_heap[0]*-1 if max_heap else 0
