class Solution:

    """
        Below we have neetcode optimal soltution
        Time Complexity:    O(n)
        Space Complexity:   O(1)
    """

    def removeDuplicates(self, nums: list[int]) -> int:
        '''
            We will use 2 pointers
            right pointer: to scan through the entire array
            left pointer: which will tell us where to place the next unique element and also how many unique elements we have seen so far, which is our output/return value 

            The idea is: 
                we compare the value at the right pointer with its predecessor. if they are different, that means that this value is the first time we're seeing it, 
                therefore it is unique.
                So we want to move it to the next unique element position which is indicated by our left pointer. Once we do that, we want to move our left pointer to the next
                unique element position.
                Differently, if the value and its predecessor are the same, it means we have already seen it and it's already in the correct unique element position. 
                So, we simply ignore it and move with the right pointer to the next element in the array.  
        '''
        # we initialize left pointer to 1 as we have seen already the first unique element, which is at position 0 in the array, i.e. the first number in the array.
        l = 1 
        # we scan the entire array with a right pointer, starting at the second element in the array
        for r in range(1, len(nums)):
            # we compare the element with its predecessor
            if nums[r] != nums[r - 1]:
                # if they are different, it means it is the first time we see this element
                # therefore, we want to move it to the next unique element position, which is indicated by our left pointer l
                nums[l] = nums[r]
                # we increment l to the next unique element position
                l +=1
        # we return the number of unique elements seen in the array
        print(nums)
        return l
    
    
        """
            Below we have my brute force solution 
            Time Complexity: O(n^2) in the worst case.  
            Space Complexity: O(1)
        """

        def myBruteForceSolution(self, nums: list[int]) -> int:
            i, j = 0,1
            while(i <= len(nums) - 2 and j <= len(nums) - 1):
                if nums[i] == nums[j]:
                    nums.pop(i)
                else:
                    i = j
                    j += 1
            return len(nums)
    
if __name__ == "__main__":
    sol = Solution()
    nums = [1,1,2]

    print("Test 1")
    print("nums: ", nums)

    print("Output Test 1: ", sol.removeDuplicates(nums=nums))

    print("-------------------------")

    nums2 = [0,0,1,1,1,2,2,3,3,4]
    print("Test 2")
    print("nums: ", nums2)

    print("Output Test 2: ", sol.removeDuplicates(nums=nums2))