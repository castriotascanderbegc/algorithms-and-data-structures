""" 
    Q: Decode Ways
    A string consisting of uppercase english characters can be encoded to a number using the following mapping:
    
    'A' -> "1"
    'B' -> "2"
    ...
    'Z' -> "26"

    To decode a message, digits must be grouped and then mapped back into letters using the reverse of the mapping above. There may be multiple ways to decode a message. For example, "1012" can be mapped into:

    "JAB" with the grouping (10 1 2)
    "JL" with the grouping (10 12)
    The grouping (1 01 2) is invalid because 01 cannot be mapped into a letter since it contains a leading zero.

    Given a string s containing only digits, return the number of ways to decode it. You can assume that the answer fits in a 32-bit integer.

"""

class Solution:
    # Below is the Brute Force solution using recursion
    # Time Complexity: T(n) = O(2^n) where n: length of the string
    def numDecodingsBruteForce(self, s: str) -> int:
        def dfs(i: int) -> int:
            # if we reached the end of the string, we can return 1
            if i == len(s):
                return 1
            # if current char is a 0, then the string is invalid
            if s[i] == '0':
                return 0
            
            # recursively process next digit
            res = dfs(i + 1)

            ### combine two digits ###

            # if we have another digit to process, i.e. double digit number
            if i + 1 < len(s):
                # check if the first digit is a 1, in this case the second digit can be anything from 0-9
                if (s[i] == '1' or 
                # if the first digit is a 2, the second digit can be anything from 0-6
                (s[i] == '2' and s[i + 1] < '7')):
                    # recursively process next digit also
                    res += dfs(i + 2)
            
            return res

        return dfs(0)
    
    # Below is the a better solution using memoization, i.e. cache TOP-DOWN approach
    # Time Complexity: T(n) = O(n) where n: length of the string
    # Space Complexity: S(n) = O(n) where n: size of the cache
    def numDecodingsMemoization(self, s: str) -> int:
        
        cache = {
            len(s): 1
        }

        def dfs(i: int) -> int:
            # if our current index is already in cache, return its value
            if i in cache:
                return cache[i]
            # if current char is a 0, then the string is invalid
            if s[i] == '0':
                return 0
            
            # recursively process next digit
            res = dfs(i + 1)

            ### combine two digits ###

            # if we have another digit to process, i.e. double digit number
            if i + 1 < len(s):
                # check if the first digit is a 1, in this case the second digit can be anything from 0-9
                if (s[i] == '1' or 
                # if the first digit is a 2, the second digit can be anything from 0-6
                (s[i] == '2' and s[i + 1] < '7')):
                    # recursively process next digit also
                    res += dfs(i + 2)
            
            # cache the result before returning it
            cache[i] = res
            return res

        return dfs(0)
    
    # Below is the the optimal solution using dynamic programming, i.e. BOTTOM-UP approach
    # Time Complexity: T(n) = O(n) where n: length of the string
    # Space Complexity: S(n) = O(n) where n: size of the cache
    def numDecodingsSpaceOptimized(self, s: str) -> int:
        dp = dp2 = 0
        dp1 = 1
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp = 0
            else:
                dp = dp1

            if i + 1 < len(s) and (s[i] == "1" or
            s[i] == "2" and s[i + 1] in "0123456"
            ):
                dp += dp2
            dp, dp1, dp2 = 0, dp, dp1
        return dp1
