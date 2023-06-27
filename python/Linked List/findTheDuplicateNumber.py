class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # O(n) O(1)
        # linked list cycle, Floyd's tortoise and hare algorithm
        slow, fast = 0, 0 # tortoise, hare

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow
