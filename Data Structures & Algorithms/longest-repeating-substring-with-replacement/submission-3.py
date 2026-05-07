class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        count = defaultdict(int)
        left = 0
        maxFreq = 0
        for right in range(len(s)):
            count[s[right]] += 1
            maxFreq = max(maxFreq, count[s[right]])
            while right-left+1 - maxFreq > k:
                count[s[left]] -= 1
                left += 1
            max_len = max(max_len, right-left+1)
        return max_len
