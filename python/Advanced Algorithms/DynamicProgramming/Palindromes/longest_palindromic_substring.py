"""
    Q:  Given a string s, return the longest substring of s that is a palindrome.
        A palindrome is a string that reads the same forward and backward.
        If there are multiple palindromic substrings that have the same length, return any one of them.

"""


class Solution:
    # Using Two Pointers Technique with a DP approach
    def longestPalindrome(self, s: str) -> str:
        resIdx = 0  # initialize starting point of our result
        resLen = 0  # initialize len of our result

        # traverse entire string
        for i in range(len(s)):

            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # check if current length is greater than max so far
                if (r - l + 1) > resLen:
                    # update starting point of word with max length
                    resIdx = l
                    # update max length
                    resLen = r - l + 1
                l -= 1
                r += 1

            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resIdx = l
                    resLen = r - l + 1
                l -= 1
                r += 1

        return s[resIdx : resIdx + resLen]
        