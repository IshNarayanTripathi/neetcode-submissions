class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        newS = ""
        for i in s:
            if i.isalnum():
                newS += i
        l, r = 0, len(newS)-1
        while l < r:
            if newS[l] != newS[r]:
                return False
            l += 1
            r -= 1
        return True
