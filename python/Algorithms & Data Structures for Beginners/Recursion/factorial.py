class Solution:
    # Recursive implementation of n! (factorial) calculation
    def factorial(self, n: int) -> int:
        # Base case: n = 0 or n = 1
        if n <= 1:
            return 1
        # Recursive case: n! = n * (n - 1)!
        return n * self.factorial(n - 1)