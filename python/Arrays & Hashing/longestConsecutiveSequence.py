class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # O(n) O(n)
        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if start of sequence
            if (n-1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest
