class Solution:

    def encode(self, strs: List[str]) -> str:
        # res = ""
        # for i in strs:
        #     res += f"{len(i)}#{i}"
        # return res
        return ''.join([f'{len(i)}#{i}'  for i in strs])



    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        n = len(s)
        while i < n:
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j+1
            word = s[i:i+length]
            res.append(word)
            i += length
        return res