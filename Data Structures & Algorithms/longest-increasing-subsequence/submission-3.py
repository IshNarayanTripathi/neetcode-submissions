class Solution:
    def lengthOfLIS(self, s: List[int]) -> int:
        max_len = [1]*len(s)
        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)):
                if s[i] < s[j]:
                    max_len[i] = max(max_len[i], 1+max_len[j])
        return max(max_len)

