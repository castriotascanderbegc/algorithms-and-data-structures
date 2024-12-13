class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    # Time Complexity: O(1)
    def insert(self, word: str) -> None:
        curr = self.root    # start at the root TrieNode
        # iterate over the characters of the given input word to insert
        for c in word:
            # if the character has not been inserted yet
            if c not in curr.children:
                # insert the character
                curr.children[c] = TrieNode()
            # move the pointer to the next char, i.e. TrieNode
            curr = curr.children[c]
        # set last character as the end of the word
        curr.word = True
    
    # Time Complexity: O(1)
    def search(self, word: str) -> bool:
        curr = self.root    # start at the root TrieNode
        # iterate over the characters of the given input word to search for
        for c in word:
            # if the character is not present, return False
            if c not in curr.children:
                return False
            # move the pointer to the next char, i.e. TrieNode
            curr = curr.children[c]
        # check whether last character is the ned of the word
        return curr.word

    # Time Complexity: O(1)
    def startsWith(self, prefix: str) -> bool:
        curr = self.root    # start at the root TrieNode
        # iterate over the characters of the given input word to search for
        for c in prefix:
            # if the character is not present, return False
            if c not in curr.children:
                return False
            # move the pointer to the next char, i.e. TrieNode
            curr = curr.children[c]
        # all the chars within prefix are in our Trie
        return True


