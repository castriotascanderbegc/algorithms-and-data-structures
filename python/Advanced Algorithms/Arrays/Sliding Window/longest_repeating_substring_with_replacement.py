"""
    Q: You are given a string s consisting of only uppercase english characters and an integer k. 
    You can choose up to k characters of the string and replace them with any other uppercase English character.
    After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

"""
class Solution:
    """
        The idea here is to use a map to track the most frequent character in the string. 
        We can then use this map with a fixed size Sliding Window approach to get our final result. 

        Using two pointers L and R, we keep expanding our window, i.e. increment R, until the following is true: 

        current size of the window (R - L + 1) - count of most frequent character in the string <= k replacements.

        Steps: 
            1. add current char to the map / increment its count in the map
            2. if condition is not valid anymore , decrement count of char at L in the map and increment pointer L
            3. keep track of the current max

        Time Complexity: O(26n) --> O(n)
    """
    def characterReplacement(self, s: str, k: int) -> int:
        frequencies = dict()        # initialize a map
        res = 0                     # initialize our result

        L = 0                       # initialize L pointer
        
        # move with R pointer through the string
        for R in range(len(s)):
            # add current char in the map / increment its count in the map
            frequencies[s[R]] = 1 + frequencies.get(s[R], 0)

            # until current length of the window - count of most frequent char in the string <= k, keep expanding the window with R
            # however, if condition is not valid anymore decrement count of char at L in the map, and increment L
            while (R - L + 1) - max(frequencies.values()) > k:
                frequencies[s[L]] -= 1
                L += 1

            # keep track of the current max
            res = max(res, R - L + 1)
        
        # return res
        return res

    
    """
        Below represents an optimization by keeping track of the current most frequent character in the string
        rather than using max(frequencies.values()). 

        This will be O(n)
    """
    
    def characterReplacementOptimized(self, s: str, k: int) -> int:
        frequencies = dict()
        res = 0

        L = 0
        maxF = 0                    # keep track of the current most frequent
        for R in range(len(s)):
            frequencies[s[R]] = 1 + frequencies.get(s[R], 0)
            maxF = (maxF, frequencies[s[R]])    # update current most frequent

            # we can do the same as we did above using maxF, i.e current most frequent char in the string
            while (R - L + 1) - maxF > k:
                frequencies[s[L]] -= 1
                L += 1

            res = max(res, R - L + 1)
        
        return res



        