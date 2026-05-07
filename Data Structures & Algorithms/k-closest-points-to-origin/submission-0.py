class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = [x**2+y**2 for x,y in points]
        res = list(zip(points, dist))
        res.sort(key=lambda x: x[1])
        return [res[i][0] for i in range(k)]