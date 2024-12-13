"""
    Palindromes. Q: Given a string S, return the length of the longest palindromic substring within S.

"""

class Palindromes:
    # Dynamic Programming Approach
    # Time: O(n^2), Space: O(n)
    def longest(self, s: str) -> int:
        length = 0              # initialize our result
        # loop over the string s
        for i in range(s):
            # odd length
            # set pointers at the current character
            left, right = i, i
            # as long as our pointers are not out of bounds, and 
            # s[left] == s[right], then we can expand out
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > length:
                    length = right - left + 1
                    ### we can also do the following:
                    #length = max(right - left + 1, length)
                left -= 1
                right += 1
            

            # even length
            # set left at the current character, and right at the next character
            left, right = i, i + 1
            # as long as our pointers are not out of bounds, and 
            # s[left] == s[right], then we can expand out
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > length:
                    length = right - left + 1
                    ### we can also do the following:
                    #length = max(right - left + 1, length)
                left -= 1
                right += 1

        return length
    
    def refactoredLongest(self, s: str) -> int:
        length = 0
        for i in range(len(s)):
            # odd length
            length = max(length, self.helper(s, i, i))

            # even length
            length = max(length, i, i + 1)
            
        return length

    def helper(self, s: str, left: int, right: int) -> int:
        res = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if (right - left + 1) > res:
                res = right - left + 1
            left -= 1
            right += 1
        return res





