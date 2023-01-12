# time O(n) space O(n)

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # use hashset 
        # hashset stores a value using a hash table 
        hashset = set()
        
        # check if the number is in hashset
        for n in (nums):
            if n in hashset:
                return True
            # add to hashset
            hashset.add(n)
        # return false if tehre were no duplicates in hashset
        return False
