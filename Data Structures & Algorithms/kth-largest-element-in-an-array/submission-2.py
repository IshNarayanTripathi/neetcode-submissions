class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [-i for i in nums]
        heapq.heapify(max_heap)
        val = 0
        while k > 0:
            val = heapq.heappop(max_heap)
            k -= 1
        return -val
