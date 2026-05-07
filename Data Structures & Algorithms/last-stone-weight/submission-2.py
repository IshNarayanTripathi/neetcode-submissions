class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.min_heap = [-i for i in stones]
        heapq.heapify(self.min_heap)
        while len(self.min_heap) > 1:
            x = heapq.heappop(self.min_heap)
            y = heapq.heappop(self.min_heap)
            if abs(x) == abs(y):
                continue
            new_val = abs(abs(x)-abs(y))
            heapq.heappush(self.min_heap, -new_val)
        return -self.min_heap[0] if self.min_heap else 0
