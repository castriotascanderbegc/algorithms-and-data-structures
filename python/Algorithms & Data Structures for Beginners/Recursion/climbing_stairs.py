class Solution:
    """
    We can either use 1 step or 2 steps --> Draw a decision tree

    The idea here is to either use recursion, for a brute force solution. 
    With recursion, using DFS, we can draw out the decision tree and the time complexity will be T(n) = O(2^n)
    where n = height of the decision tree. 

    This will look like exactly the fibonacci sequence. 1, 1, 2, 3, 5, 8, 13, 21...
    Where we use the 2 previous numbers to compute the next one. 

    n => 1

    f(n) = f(n - 1) + f(n - 2)
    f(0) = 1
    f(1) = 1
    f(2) = 2
    f(3) = f(2) + (1) = 2 + 1 = 3

    An optimal solution, instead, will be using DP - dynamic programming with a bottom-up approach. 
    We can start from the base case, and work our way up to the solution. 

    Using two variables, we can shift them n - 1 times calculating their sum. 

    For example, if we need to compute n = 5. 
    We can start from 5. From 5, we only need 1 step to reach our solution 5. 
    We can move up to 4. From 4, we only need 1 step to reach our solution 5.
    We can move up to 3. From 3, we only need 2 steps to reach our solution 5. 
    But we already computed steps at point 4 and point 5. So the result will be 1 + 1 = 2. 
    We can move up to 2. From 2, we only need 3 steps to reach out solution 5. 
    But we already computed steps at point 3 and 4. So the result will be 2 + 1 = 3. 

    And so on..
     
    """
    def climbStairsRecursively(self, n: int) -> int:
        # base cases
        # if we have either 1 or 2 steps, we can climb in either 1 or 2 ways, i.e. 1 step or 3 steps 
        if n == 1 or n == 2:
            return n
        
        # our result will be the sum of the 2 previous solutoins 
        # this is the fibonacci sequence, 1, 1, 2, 3, 5, 8, 13, 21.. 
        prev = self.climbStairs(n - 1)
        prevPrev = self.climbStairs(n - 2)
        return prev + prevPrev

    def climbStairs(self, n: int) -> int:
        # our base cases 
        if n <= 3:
            return n
        
        # let's initialize two variables to our last base cases
        n1, n2 = 2, 3
        # shift the two variables up to n
        for i in range(4, n + 1):
            temp = n2            # store current second variable value before shifting
            n2 = n2 + n1         # move second variable by computing sum with itself and previous variable
            n1 = temp            # move first variable to original second variable
        return n2                # simply return our second varible which will hold the result at i == n