class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest = 0
        res = set()
        for right in range(len(s)):
            while s[right] in res:
                res.remove(s[left])
                left +=  1
            res.add(s[right])
            longest = max(longest, right-left+1)
        return longest