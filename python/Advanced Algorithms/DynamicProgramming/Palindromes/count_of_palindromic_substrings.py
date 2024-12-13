"""
    Q: Given a string s, return the number of substrings within s that are palindromes.
    A palindrome is a string that reads the same forward and backward.
"""
class Solution:
    # Two Pointers technique in a DP fashion
    # Time Complexity: T(n) = O(n^2)
    # Space Complexiry: S(n) = O(1)
    def countSubstrings(self, s: str) -> int:
        res = 0     # initialize our count of palindromic substring

        # traverse entire string
        for i in range(len(s)):

            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # increment palindromic substring count
                res += 1
                # decrement left
                l -= 1
                # increment right
                r += 1

            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # increment palindromic substring count
                res += 1
                # decrement left
                l -= 1
                # incremenent right
                r += 1

        return res
        