class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1, l2 = 0, 0
        res = ""
        alternate = 0
        while l1 < len(word1) and l2 < len(word2):
            if alternate % 2 == 0:
                res += word1[l1]
                l1 += 1
                alternate += 1
            else:
                res += word2[l2]
                l2 += 1
                alternate += 1
        if l1 < len(word1):
            res += word1[l1:]
        if l2 < len(word2):
            res += word2[l2:]
        return res