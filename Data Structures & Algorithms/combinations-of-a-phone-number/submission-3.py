class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitsToChar = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        res = []
        def dfs(ind, curr):
            if len(curr) == len(digits):
                if curr:
                    res.append(''.join(curr.copy()))
                return
            for char in digitsToChar[digits[ind]]:
                curr.append(char)
                dfs(ind+1, curr)
                curr.pop()
        dfs(0, [])
        return res