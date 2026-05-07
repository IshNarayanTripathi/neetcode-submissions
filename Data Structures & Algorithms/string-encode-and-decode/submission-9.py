class Solution:
    def encode(self, strs: list[str]) -> str:
        res = ''
        for string in strs:
            res += f'{len(string)}#{string}'
        return res

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            word = s[j+1:j+length+1]
            res.append(word)
            i = j+length+1
        return res