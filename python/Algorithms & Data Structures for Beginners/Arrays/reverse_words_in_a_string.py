"""
    Q: Reverse Words in a String III

    Given a string s, reverse the order of characters in each word within
    a sentence while still preserving whitespace and initial word order.
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        # split the input string s by whitespace
        s_list = s.split(" ")

        # iterate over the words in the list
        for index, word in enumerate(s_list):
            s_list[index] = word[::-1]
        
        # convert the list back to a string
        res = ""
        for word in s_list:
            res += word
            # preserve original whitespaces
            res += " "
        
        # return the res, ignore last whitespace char
        return res[:-1]
