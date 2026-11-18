class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}
        w1, w2 = len(word1), len(word2)
        def traverse(i, j):
            if i == w1 and j == w2:
                return 0
            elif i == w1: 
                return w2-j
            elif j == w2:
                return w1-i
            if (i, j) in dp:
                return dp[(i, j)]
            res = 0
            if word1[i] == word2[j]:
                res += traverse(i+1, j+1)
            else:
                res += min(1+traverse(i+1, j), 1+traverse(i, j+1), 1+traverse(i+1, j+1))
            dp[(i, j)] = res
            return dp[(i, j)]
        return traverse(0, 0)
             