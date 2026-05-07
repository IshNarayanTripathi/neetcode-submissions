class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        max_heap = [(-freq, i) for  i, freq in count.items()]
        heapq.heapify(max_heap)
        res = []
        while k:
            _, key = heapq.heappop(max_heap)
            res.append(key)
            k-=1
        return res