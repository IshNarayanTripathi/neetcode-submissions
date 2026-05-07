class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = Counter(nums)
        longest = 0
        for num in nums:
            curr_val = num
            curr_len = 1
            while curr_val+1 in count:
                curr_val += 1
                curr_len += 1
            longest = max(longest, curr_len)
        return longest
