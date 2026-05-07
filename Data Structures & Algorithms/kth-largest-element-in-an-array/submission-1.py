class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.min_heap = [-i for i in nums]
        heapq.heapify(self.min_heap)
        while k-1>0:
            heapq.heappop(self.min_heap)
            k-=1
        return -self.min_heap[0]