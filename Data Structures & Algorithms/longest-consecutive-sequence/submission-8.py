class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s = set(nums)
        max_val = 1
        for i in nums:
            if i - 1 not in s:
                
                val = i
                curr = 1
                while val+1 in s:
                    curr += 1
                    val += 1
                    max_val = max(max_val, curr)
        return max_val