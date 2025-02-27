"""
    Q: Permutation in String

    You are given two strings s1 and s2.

    Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.

    Both strings only contain lowercase letters.
"""
class Solution:
    """
        The idea here is to use a HashMap to count the frequencies of each character in string s1.
        We can then use a sliding window technique on string s2 with a fixed window size equal to the length of string s1.
        To track the current window, we maintain a running frequency count of characters in s2. This count represents the chars in the current window. 
        At each step, if the frequency count matches that of s1, we return true.
    """
    # Time Complexity: T(n) = O(n * m) where n = lenght of s1 and m = lenght of s2
    # Space Complexity: S(n) = O(1), constant because map can be at most of 26 keys
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # initialize character frequency map for s1
        count1 = dict()
        
        # iterate over the characters in s1 to update s1 frequency map
        for c in s1:
            count1[c] = 1 + count1.get(c, 0)

        # our fixed size window is the length of s1
        target = len(count1)
        
        # iterate over the string s2
        for i in range(len(s2)):
            # keep a running frequency map of s2 and count of char matches
            count2, curr = dict(), 0
            # update character frequency map in string s2
            for j in range(i, len(s2)):
                count2[s2[j]] = 1 + count2.get(s2[j], 0)
                # if count of current char in s1 is smaller that count of current char in s2, break loop execution
                if count1.get(s2[j], 0) < count2[s2[j]]:
                    break
                # if count of current char in s1 is equal that count of current char in s2, increment char matches    
                if count1.get(s2[j], 0) == count2[s2[j]]:
                    curr += 1
                # if char matches is equal to our target, we can immediately return true
                if curr == target:
                    return True
        # we haven't found a solution yet, so we return false
        return False


                
