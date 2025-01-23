"""
    Q: Given two integers a and b, return the sum of the two integers without using the + and - operators.
"""
class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32 bit mask in hexadecimal --> this is specifically needed in Python because Python's int numbers are not 32bits
        mask = 0xffffffff

        # Repeat until our carry is equal to 0 
        while (b & mask) != 0:
            # calcuate a + b with carry --> (a & b) shifted left by 1
            carry = (a & b) << 1

            # calculate a + b without carry --> a XOR b
            a = (a ^ b)

            # update b to the carry
            b = carry

        return (a & mask) if b > 0 else a
        