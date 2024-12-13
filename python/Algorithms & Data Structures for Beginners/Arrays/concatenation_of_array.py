class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        # call n the length of the input array nums
        n = len(nums)
        # create an array of length 2n
        ans = [0] * n * 2
        # move through the input array nums
        for i in range(len(nums)):
            # we want to set:
            #   ans[i] == nums[i]
            #   ans[i + n] == nums[i]
            ans[i], ans[i + n] = nums[i], nums[i]
        return ans
    
if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,1]

    print("Test 1")
    print("nums: ", nums)

    print("Output Test 1: ", sol.getConcatenation(nums=nums))

    print("-------------------------")

    nums2 = [1, 3, 2, 4, 5]
    print("Test 2")
    print("nums: ", nums2)

    print("Output Test 2: ", sol.getConcatenation(nums=nums2))