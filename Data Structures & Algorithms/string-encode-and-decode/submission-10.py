class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += f"{len(word)}#{word}"
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j+1] != "#":
                j += 1
            length = int(s[i:j+1])
            i = j+2
            word = s[i:i+length]
            res.append(word)
            i = i+length
        return res
