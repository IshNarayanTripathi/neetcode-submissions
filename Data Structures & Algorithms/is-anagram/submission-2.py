from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counta = Counter(s)
        countb = Counter(t)
        return counta == countb