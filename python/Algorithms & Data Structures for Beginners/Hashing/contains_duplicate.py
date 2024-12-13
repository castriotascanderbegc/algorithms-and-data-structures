class Solution:
    """
        Brute force: we could look at each number and see if there's a duplicate in the array. It is a two pass on the array.
            It will take us O(n^2) time complexity and O(1) space
        Better implementation: we could sort the array and then have a single pass on the array since if any duplicates are present they will be adjacent to each other.
            It will take us O(n log n) time complexity to sort the array and look for the adjacent and O(1) space
        
        Best implementation: Either use a HashSet or HashMap where we can insert and search in O(1). 
            In this case, we can have a single pass on the array and for each number we either insert in the HashSet/HashMap or if the number is already
            present we know it is a duplicate so we return. 

                This solution takes us O(n) time complexity and O(n) space complexity
    """

    # HashSet implementation, better suited for this problem. We don't really need a key-value pair
    def hasDuplicate(self, nums: list[int]) -> bool: 
        hashSet = set()

        for n in nums:
            if n in hashSet:
                return True
            hashSet.add(n)

        return False


    # HashMap implementation
    def containsDuplicate(self, nums: list[int]) -> bool:
        count = {}

        for n in nums:
            if n not in count:
                count[n] = 1
            else:
                return True
    
        return False