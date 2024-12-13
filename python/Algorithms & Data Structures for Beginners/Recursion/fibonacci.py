class Solution:
    # Recursive implementation to calculate the n-th Fibonacci number
    def fibonacci(self, n: int) -> int:
        # Base case: n = 0 or n = 1
        if n <= 1:
            return n
        # Recursive case: fib(n) = fib(n - 1) + fib(n - 2)
        return self.fibonacci(n - 1) + self.fibonacci(n - 2)
        