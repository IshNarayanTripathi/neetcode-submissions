class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        res = []
        max_heap = [(-freq, key) for key, freq in count.items()]
        heapq.heapify(max_heap)
        while k:
            _, key = heapq.heappop(max_heap)
            res.append(key)
            k -= 1
        return res