"""
    Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
    Notice that the solution set must not contain duplicate triplets.

"""
class Solution:
    # Optimal Solution using two pointers technique and sorting the input array
    # Time Complexity: O(n log n) + O(n^2) ---> reduces to O(n^2)
    # Space Complexity: O(n) or O(1) depending on the sort() when we are sorting the input array
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        # n + l + r = 0

        res = []
        nums.sort()     # sort the input array

        # repeat the two-sum II problem
        for i, n in enumerate(nums):
            # we cannot have duplicate triplets
            # check whether we are looking at a number n we already looked at the same position
            if i > 0 and n == nums[i - 1]:
                continue
            
            L, R = i + 1, len(nums) - 1     # initialize left and right pointers

            # move pointers until they cross
            while L < R:
                # compute the threeSum using L, R, and n
                threeSum = n + nums[L] + nums[R]
                # if sum greater than our target, decrement right pointer
                if threeSum > 0:
                    R -= 1
                # if sum smaller than our target, increment left pointer
                elif threeSum < 0: 
                    L += 1
                # we found a triplet
                else:
                    # append the triplet to the result
                    res.append([n, nums[L], nums[R]])
                    # increment left pointer to avoid looking at the same numbers
                    L += 1
                    # keep on incrementing the left pointer if we are seeing the same number in the same position
                    while nums[L] == nums[L - 1] and L < R:
                        L += 1
        
        # return our result
        return res
