import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = []
        self.k = k

        for num in nums:
            self.add(num)  # Use logic from `add()` to avoid duplicate code

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        elif val > self.min_heap[0]:
            heapq.heappushpop(self.min_heap, val)
        # else: ignore the value, it's not in the top k

        return self.min_heap[0]
