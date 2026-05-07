class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        i = 0
        n = len(intervals)
        while i < n:
            new = intervals[i]
            while i + 1 < n and intervals[i+1][0] <= new[1]:
                new[0] = min(new[0], intervals[i+1][0])
                new[1] = max(new[1], intervals[i+1][1])
                i+=1
            res.append(new)
            i+=1
        return res