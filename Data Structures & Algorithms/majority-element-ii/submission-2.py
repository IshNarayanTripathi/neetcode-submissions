class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        n = len(nums)
        res = []
        for key, val in count.items():
            if val > n/3:
                res.append(key)
        return res