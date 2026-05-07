class Solution:
    def lengthOfLIS(self, s: List[int]) -> int:
        max_lis = [1]*len(s)
        for i in range(len(s)-1, -1, -1):
            
            for j in range(i+1, len(s)):
                if s[i] < s[j]:
                    max_lis[i] = max(max_lis[i], 1+max_lis[j])
        return max(max_lis)