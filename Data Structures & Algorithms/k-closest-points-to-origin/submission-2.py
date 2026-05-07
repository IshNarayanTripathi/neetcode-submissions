class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.min_heap = [(point[0]**2+point[1]**2, point) for point in points]
        heapq.heapify(self.min_heap)
        res = []
        while k > 0:
            _, point = heapq.heappop(self.min_heap)
            res.append(point)
            k-=1
        return res