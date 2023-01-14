# One pass | time: O(n) | mem: O(n)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        prevMap = {} # val : index
        
        for i, n in enumerate(nums): # loops though the index (i) and the element (n)
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i


# Brute Force | time: O(n^2) 
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for n in range(len(nums)):
            for i in range(len(nums)):
                if nums[i] + nums[n] == target and n!=i:
                    return n,i
