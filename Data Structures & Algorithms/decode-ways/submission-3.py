class Solution:
    def numDecodings(self, s: str) -> int:
        count = 0
        def backtrack(ind, path):
            nonlocal count
            if ind >= len(s):
                count += 1
                return
            if s[ind] != '0':
                one = s[ind]
                backtrack(ind+1, path+[one])
            if ind+1 < len(s) and s[ind] != '0':
                
                two = s[ind:ind+2]
                if 1 <= int(two) <= 26:
                    backtrack(ind+2, path+[two]) 
        backtrack(0, [])
        return count