class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        l = []
        for interval in intervals:
            if not l or l[-1][1] < interval[0]:
                l.append(interval)
            else:
                l[-1][1] = max(l[-1][1], interval[1])
        return l
                