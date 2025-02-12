"""
    Q: Evaluate Reverse Polish Notation

    You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.

    Return the integer that represents the evaluation of the expression.

    The operands may be integers or the results of other operations.
    The operators include '+', '-', '*', and '/'.
    Assume that division between integers always truncates toward zero.

"""

from typing import List


class Solution:
    """
        The idea here is to use a stack to efficiently benefit from push and pop operations in O(1) time. 
        This way we can have a single pass on the given input array of tokens.

        We can use a stack. We iterate through the array, and if we encounter a number, we push it onto the stack. 
        If we encounter an operator, we pop two elements from the stack, treat them as operands, and solve the equation using the current operator. 
        Then, we push the result back onto the stack

        Since the given array has a postfix expression, the stack helps us to maintain the correct order of operations
        by ensuring that we always use the most recent operands (those closest to the operator) when performing the operation.
        After the iteration, the final result is left in the stack.
    """
    # Time Complexity: T(n) = O(n)
    # Space Complexity: S(n) = O(n)
    def evalRPN(self, tokens: List[str]) -> int:
        # initalize our stack
        stack = []
        # have a set of operators
        operators = set(["*", "-", "+", "/"])
        # iterate through the given array of tokens
        for token in tokens:
            # if current token is a number simply push it on the stack
            if token not in operators:
                stack.append(int(token))
            else: # if an operator

                # push the two operands from the stack
                rightOperand = stack.pop() 
                leftOperand = stack.pop()
                
                # perform the correct operation
                if token == "*":
                    curr_res = leftOperand * rightOperand
                elif token == "-":
                    curr_res = leftOperand  - rightOperand
                elif token == "+":
                    curr_res = leftOperand + rightOperand
                else:
                    curr_res = int(leftOperand / rightOperand)
                
                # append the result on the stack
                stack.append(curr_res)
        
        # the final result will be on top of the stack
        return stack.pop()


