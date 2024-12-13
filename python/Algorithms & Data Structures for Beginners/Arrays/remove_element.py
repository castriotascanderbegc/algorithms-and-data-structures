class Solution:

    """
        The idea is:
            We are going to use 2 pointers: 
                1. Pointer to scan through the entire array, i.e. pointer i
                2. Pointer which should tell us the location where we should place the next element in the array we see that is not equal to val, i.e. pointer 2

    We would like to move all the elements in the array which ARE NOT val at the beginning of the array. By "removing" we mean move them in place, not deleting them from the array.

    So we scan the array with one pointer and check if each number in the array is equal to val:
        - if a number is equal to val, we simply ignore it and move on. We don't want to do anything if we encounter val
        - if a number is not equal to val, then that's when we do something with it. We move the item we are seeing at the beginning of the array in the position specified 
        by our second pointer

    Time Complexity:    O(n) we are only stepping through the array once. 
    Space Complexity:   O(1) we are not using any extra space, requested. 
    """
    
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0                       # initialize pointer 2 at the beginning of the array
        for i in range(len(nums)):  # let's scan the entire array using pointer 1
            if nums[i] != val:      # if the current number at pointer 1, i, is not val, then we want to move it in the position specified by pointer 2, k.
                nums[k] = nums[i]
                k+=1                # we move pointer 2 forward in the array to the next available position
            
            # if the current number at pointer 1 is equal to val, we ignore it and move on. 
        
        return k                    # by the time we get to the end of the array, pointer 2, k, will tell us number of elements in the array which are not equal to val.

    # Optimized solution with the same time and space complexity
    def optimizedRemoveElement(self, nums: list[int], val: int) -> int:
        # Avoid unecessary copy operations in above solution, when k == i and nums[i] != val
        # by swapping nums[i] and the last element of the array (nums[n])
        n = len(nums)
        i = 0

        while(i < n):
            if nums[i] == val:      # if equal, move the elem at the end of the array
                nums[i], nums[n - 1] = nums[n - 1], nums[i]
                n -= 1              # decremenet the length of the array by discarding the last element
            else:
                i += 1              # if not equal, move forward
        return n
    
    def myBruteForceSolution(self, nums: list[int], val: int) -> int:
        L = 0
        R = len(nums) - 1
        k = 0
        while(L <= R):
            if nums[L] != val:
                L += 1
                k += 1
            elif nums[R] != val:
                curr = nums[L]
                nums[L] = nums[R]
                nums[R] = curr
                R -= 1
                L += 1
                k += 1
            else:
                R -= 1
        return k




if __name__ == "__main__":
    sol = Solution()
    nums = [1,1,2]
    val = 2
 
    print("Test 1")
    print("nums: ", nums)

    print("Output Test 1: ", sol.removeElement(nums=nums, val=val))

    print("-------------------------")

    nums2 = [0,0,1,1,1,2,2,3,3,4]
    val = 1
    print("Test 2")
    print("nums: ", nums2)

    print("Output Test 2: ", sol.removeElement(nums=nums2, val=val))