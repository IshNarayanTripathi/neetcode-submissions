class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordmap = [False]*(len(s)+1)
        wordmap[len(s)] = True
        for i in range(len(s)-1,-1,-1):
            for word in wordDict:
                if i +  len(word) <= len(s) and s[i:i+len(word)] == word:
                    wordmap[i] = wordmap[i+len(word)]
                if wordmap[i]:
                    break
        return wordmap[0]

