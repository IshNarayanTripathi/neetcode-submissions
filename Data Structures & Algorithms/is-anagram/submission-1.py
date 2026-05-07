class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s = Counter(s)
        count_t = Counter(t)
        for i in s:
            if count_s[i] != count_t[i]:
                return  False
        return True
        