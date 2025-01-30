"""
    Q: Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

    Please implement encode and decode

"""
class Solution:
    """
        The idea is to encode a string by using some delimeter to allow us to decode each word based on when we see the delimeter

        For example, input = ["neet", "code", "love", "you"]

        We can encode this list of words into a string where we start with the length of the word followed by # sign as our delimeter, and then we word itself.

        "4#neet4#code4#love3#you"

        This way, the number will tell us how many chars we need to read after the # sign in order to decode the word.

        Time Complexity: O(n)

    """
    def encode(self, strs: list[str]) -> str:
        res = ""        # initialize an empty string
        # read each word in the input list
        for word in strs:
            # append the length of the current word, the # sign, and the word itself
            res += str(len(word)) + "#" + word

        # return the encoded string
        return res

    """
        Pass through the encoded word with 2 pointers i and j. 

        Keep moving with j until we see the # sign. This will determine that a word will start after the # sign. 

        Since we will stop at # sign, we know that the what we have read so far is the length of the word to decode. 

        Using the length we can read the word and then update our pointers to read each next word

        Time Complexity: O(n)
    """
    def decode(self, s: str) -> list[str]:
        res = []        # initialize an empty list
        i = 0           # initialize i pointer
        # move through the characters in the word
        while i < len(s):
            j = i       # initilize j pointer initially at i
            # keep moving j until we see the # sign
            while s[j] != '#':
                j += 1
            # we stopped at the # sign, so we can first read the length of the word
            length = int(s[i:j])
            # read the word using its length and append to our result
            res.append(s[j + 1: j + 1 + length])
            i = j + 1 + length  # update our pointers
        return res

# 4#neet4#code4#love3#you
# i = 12, j = 13, length = 3
# res = ['neet', 'code', 'love', 'you']