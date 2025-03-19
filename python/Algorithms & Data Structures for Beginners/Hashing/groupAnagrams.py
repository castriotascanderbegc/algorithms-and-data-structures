"""
    Q: Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

    An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

"""

import collections


class Solution:

    # Brute force solution - Time Complexity: O(m * n log n) 
    # The idea here is to insert the sorted word as a key in our map appending each word mapping to this key
    # Will take m to traverse the input array and n log n to sort each word before inserting it as a key
    def groupAnagramsBruteForce(self, strs: list[str]) -> list[list[str]]:
        anagramsMap = collections.defaultdict(list)     # create a default dict 
        # traverse the array of strings
        for word in strs:
            # sort the word 
            sorted_word = "".join(sorted(word))    
            # map the original word (value) to the sorted word (key)
            anagramsMap[sorted_word].append(word)
        
        # return all values in the map
        return anagramsMap.values() # type: ignore
    
    # Optimal solution - Time Complexity: O(m * n)
    # The idea here is to count the occurrences of each letter for each word and insert this count as a key in our map
    # We can append each word with this characters count in the map
    # Will take m to traverse the input array and n to count the chars in the word
    # for the occurrences of the characters in the work we can use an array where i = 0 are # of 'a' chars in the word, and so on. 
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagramsMap = collections.defaultdict(list)     # create a default dict
        # traverse the array of strings
        for word in strs:
            count = [0] * 26        # initialize the count of chars, a - z
            for char in word:       # loop over the characters in the word
                # increment the count for each character
                count[ord(char) - ord("a")] += 1
            
            # map the word (value) to the count of its letters
            anagramsMap[tuple(count)].append(word)

        # return the values in our map
        return anagramsMap.values() # type: ignore
