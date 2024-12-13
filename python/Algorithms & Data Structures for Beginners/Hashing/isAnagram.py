from collections import Counter
class Solution:
    """
        The idea here is to use a HashMap to count the occurrences of each character in the two strings. 
        Then we can compare the two HashMaps to make sure they are the same, i.e. same characters and same occurrences for each char

        This solution takes O(n) time and space complexity

        What if we are being asked to tolve with O(1) space?
            We could sort the two string first and then compare them. 
            We can sort a string in O(n log n) and most sorting algorithms take O(1) space
    """
    def isAnagram(self, s: str, t: str) -> bool:
        # sorting the two string, O(n log n) time and O(1) space
        #return sorted(s) == sorted(t)

        # using Counter, O(n) time and space complexity
        #return Counter(s) == Counter(t)


        # using a HashMap, O(n) time and space complexity
        if len(s) != len(t):
            return False
        
        sCount, tCount = {}, {}

        for i in range(len(s)):
            sCount[s[i]] = 1 + sCount.get(s[i], 0)
            tCount[t[i]] = 1 + tCount.get(t[i], 0)
        
        return sCount == tCount