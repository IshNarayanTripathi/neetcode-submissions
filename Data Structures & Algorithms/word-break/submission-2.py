class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        mapi = [False]*(len(s)+1)
        mapi[len(s)] = True
        for i in range(len(s)-1,-1,-1):
            for word in wordDict:
                curr_word = s[i:i+len(word)]
                if i+len(word) <= len(s) and curr_word == word:
                    mapi[i] = mapi[i+len(word)]
                if mapi[i]:
                    break

        return mapi[0]