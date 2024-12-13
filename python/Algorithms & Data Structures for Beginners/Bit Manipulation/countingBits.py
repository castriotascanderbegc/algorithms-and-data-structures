class Solution: 
    # count the number of 1 bits in an integer n
    # Time Complexity: O(32) where 32 is the number of bits, but this is practically O(1)
    def countBits(self, n: int) -> int:
        count = 0
        while n:
            if n & 1:
                count += 1
            n = n >> 1          # same as n // 2
        return count

    # variation using mod operator
    def countBits2(self, n: int) -> int:
        count = 0
        while n:
            count += n % 2
            n = n >> 1
        return count

    # trick of anding with n - 1. This allows us to only run our while loop the # of 1's in the number n
    def countBits3(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count
    

    """
        Given an integer n, count the number of 1's in the binary representation of every number in the range [0, n].
        Return an array output where output[i] is the number of 1's in the binary representation of i.

    """

    # Time Complexity: O(n log n)
    # log n: number of times we can divide n by 2
    # n: number of times we are repeating above, range from [0, n]  
    def countBitsInArange(self, n: int) -> list[int]:
        res = []
        for i in range(n + 1):
            count = 0
            j = i
            while j:
                count += j % 2
                j = j >> 1
            res.append(count)
        return res
    

    # We can remove a lot of the repetitive work / computations by drawing out the bits representation 
    # Using dynamic programming we can see the pattern and use that to improve our solution down to O(n) linear time

    """
        i = 0: 0 0 0 0 
        i = 1: 0 0 0 1 = 1 + dp[i - 1]
        i = 2: 0 0 1 0 = 1 + dp[i - 2]
        i = 3: 0 0 1 1 = 1 + dp[i - 2]
        i = 4: 0 1 0 0 = 1 + dp[i - 4]
        i = 5: 0 1 0 1 = 1 + dp[i - 4]
        i = 6: 0 1 1 0 = 1 + dp[i - 4]
        i = 7: 0 1 1 1 = 1 + dp[i - 4]
        i = 8: 1 0 0 0 = 1 + dp[i - 8]
    """

    # each current number has 1 bit more than the number at index number - offset where offset is the current MSB
    # MSB = [1, 2, 4, 8, 16, 32, ..]
    # dp[i] = 1 + dp[i - offset] where the offset represents where we last have seen the MSB
    def countBitsLinear(self, n: int) -> list[int]:
        dp = [0] * (n + 1)
        offset = 1
        for i in range(1, n + 1):
            # check whether we reached the next MSB by multiplying current offset by 2
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp
    




    """
        Given a 32-bit unsigned integer n, reverse the bits of the binary representation of n and return the result.

        Example: 
            Input: n = 00000000000000000000000000010101
            Output:    2818572288 (10101000000000000000000000000000)
            
            Explanation: Reversing 00000000000000000000000000010101, 
            which represents the unsigned integer 21, gives us 10101000000000000000000000000000 
            which represents the unsigned integer 2818572288.
    """

    # Time Complexity: T(n): O(32) ---> O(1)
    def reverseBits(self, n: int) -> int:
        res = 0
        pos = 0
        while n:
            res += (n & 1) << (31 - pos)
            n = n >> 1
            pos += 1
        return res

    
    def reverseBits2(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n << i) & 1
            res += (bit << (31 - i)) # res = res | (bit << (31 - i))
        return res
    
    
    