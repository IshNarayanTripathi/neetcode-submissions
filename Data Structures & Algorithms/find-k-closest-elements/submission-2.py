class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        min_heap = [(abs(x-num), num) for num in arr]
        heapq.heapify(min_heap)
        res = []
        while k>0 and min_heap:
            _, key = heapq.heappop(min_heap)
            res.append(key)
            k -= 1
        res.sort()
        return res