"""
    Q: Design a data structure that supports adding new words and searching for existing words.

    Implement the WordDictionary class:

        void addWord(word) Adds word to the data structure. 
        bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. 
            word may contain dots '.' where dots can be matched with any letter.

"""

class TrieNode:

    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.isWord = True

    def search(self, word: str) -> bool:
        def dfs(index, root):
            # start at the root
            curr = root
            # move through the word using indexing
            for i in range(index, len(word)):
                c = word[i]
                # if character is a ".", we need to skip it and backtrack any possible word in the Trie
                if c == ".":
                    # backtracking
                    # recursively backtrack on each child of the current node
                    for child in curr.children.values():
                        # skip the "." char, so pass i + 1 as the index
                        if dfs(i + 1, child):
                            # if we found a word, return True
                            return True
                    # if we could not find a word, return False
                    return False

                # character is not a ".", perform regular Trie search
                else:
                    # if character not present, return False immediately
                    if c not in curr.children:
                        return False
                    # move down the Trie
                    curr = curr.children[c]
                    
            # check whether last char is the end of a word
            return curr.isWord
        
        return dfs(0, self.root)