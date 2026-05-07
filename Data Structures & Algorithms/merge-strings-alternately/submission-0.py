class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1, p2 = 0, 0
        res = ""
        isFirst = 0
        while p1 < len(word1) and p2 < len(word2):
            if isFirst % 2 == 0:
                res += word1[p1]
                p1+=1
            else:
                res += word2[p2]
                p2+=1
            isFirst+=1
        while p1 < len(word1):
            res+=word1[p1]
            p1+=1
        while p2 < len(word2):
            res+=word2[p2]
            p2+=1
        return res