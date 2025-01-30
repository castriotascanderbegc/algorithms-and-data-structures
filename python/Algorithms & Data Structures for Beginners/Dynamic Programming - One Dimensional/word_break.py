"""
    Q: Word Break

    Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of dictionary words.
    You are allowed to reuse words in the dictionary an unlimited number of times. You may assume all dictionary words are unique.
"""
from typing import List


class Solution:
    # Top-Down approach with a cache
    # Time Complexity: T(n) = O(n * m * t)
    # Space Complexity: S(n) = O(n)
    # n: length of the string s, m is the number of words in the wordDict and t is the max. length of any word in wordDict
    def wordBreakTopDown(self, s: str, wordDict: List[str]) -> bool:
        # we first create a cache to save previous work
        cache = {
            len(s): True
        }
    
        def dfs(i):
            # if index i already in our cache, return its value
            if i in cache:
                return cache[i]
            # iterate over each word in the wordDict
            for word in wordDict:
                # if we can find this word in the string using the length of the word
                if ((i + len(word)) <= len(s) and 
                s[i: i + len(word)] == word):
                    # recursively process next
                    if dfs(i + len(word)):
                        # cache the result
                        cache[i] = True
                        # we can return here
                        return True
            cache[i] = False
            return False

        return dfs(0)
    
    # Bottom-Up approach, dynamic programming
    # Time Complexity: T(n) = O(n * m * t)
    # Space Complexity: S(n) = O(n)
    # n: length of the string s, m is the number of words in the wordDict and t is the max. length of any word in wordDict
    def wordBreakBottomUp(self, s: str, wordDict: List[str]) -> bool:
        # first create our cache to retrieve previous work done
        dp = [False] * (len(s) + 1)
        # set end of the tring as True
        dp[len(s)] = True

        # iterate over the characters in the string, from the back
        for i in range(len(s) - 1, -1, -1):
            # check each word in the dict
            for w in wordDict:
                # check if the current word is present in the string using the length of the current word
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    # if so, cache the result
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]

