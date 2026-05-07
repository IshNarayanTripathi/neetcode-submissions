class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = max_count = float("-inf")
       
        left = 0
        count = defaultdict(int)
        for right in range(len(s)):
            count[s[right]] += 1
            max_count = max(max_count, count[s[right]])
                
            while right-left+1-max_count > k:
                count[s[left]] -= 1
                left += 1

            max_len = max(max_len, right-left+1)
        return max_len