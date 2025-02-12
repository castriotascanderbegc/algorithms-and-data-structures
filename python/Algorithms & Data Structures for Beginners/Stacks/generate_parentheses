"""
    Q: Generate Parentheses

    You are given an integer n. Return all well-formed parentheses strings that you can generate with n pairs of parentheses.

"""
from typing import List


class Solution:
    """
        Here we can use backtracking following few rules when the string is invalid.

        Only add open parenthesis if the count of open < n
        Only add a closing paranthesis if the count of close < open
        The string is valid IIF count of open == count of close
    """
    def generateParenthesis(self, n: int) -> List[str]:
        # initialize our result
        res = []
        # initialize our stack, will maintain the ()
        stack = []

        def backtrack(openN, closeN):
            # string is valid
            if openN == closeN == n:
                res.append("".join(stack))
                return
            
            # we can add an open parenthesis
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closeN)
                stack.pop()
            
            # we can add a close parenthesis
            if closeN < openN:
                stack.append(")")
                backtrack(openN, closeN + 1)
                stack.pop()

        backtrack(0,0)
        return res