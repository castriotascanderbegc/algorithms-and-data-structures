"""
    Q: You are given a string digits made up of digits from 2 through 9 inclusive.
    
    Each digit (not including 1) is mapped to a set of characters as shown below:

    A digit could represent any one of the characters it maps to.

    Return all possible letter combinations that digits could represent. You may return the answer in any order.

"""

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # harcode digit to char map
        digits_map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        res = []    # initialize our result

        def helper(i, comb):
            # if len of current combination is same as digits
            if len(comb) == len(digits):
                # we can append to our result
                res.append(comb)
                return
            
            # for each character combination within a digit
            # i.e. 2: a, b, c
            for char in digits_map[digits[i]]:
                # we want to backtrack by moving to next digit
                # and adding current character to the current combination
                helper(i + 1, comb + char)

        # if digits != "", execute backtracking
        if digits:
            helper(0, "")

        return res


