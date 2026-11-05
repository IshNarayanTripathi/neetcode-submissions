from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        sc = sorted(count, key = lambda x: (count[x], x), reverse=True)
        res = []
        i = 0
        for key in sc:
            if i == k:
                break
            res.append(key)
            i += 1
        return res