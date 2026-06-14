class Solution:
    def validPalindrome(self, s: str) -> bool:
        s1 = ""
        for c in s:
            if c.isalnum():
                s1 += c
        for i in range(len(s1)):
            res = s1[:i]+s1[i+1:]
            rev = "".join(reversed(res))
            if res == rev:
                return True
        return False