class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = [(i[0]**2+i[1]**2, i)  for i in points]
        heapq.heapify(min_heap)
        res = []
        while k > 0:
            _, i = heapq.heappop(min_heap)
            res.append(i)
            k -= 1
        return res
            