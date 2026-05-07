class Node:
    def __init__(self):
        self.children = {}
        self.eow = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.eow = True

    def search(self, word: str) -> bool:
        def dfs(root, ind):
            curr = root
            for j in range(ind, len(word)):
                letter = word[j]
                if letter == ".":
                    for child in curr.children.values():
                        if dfs(child, j+1):
                            return True
                    return False
                else:
                    if letter not in curr.children:
                        return False
                    curr = curr.children[letter]

            return curr.eow
        return dfs(self.root, 0)
                

