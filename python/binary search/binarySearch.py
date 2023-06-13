    class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # O(logn)
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + ((r - l) // 2) # instead of mid = (r+l)//2 so it won't  overflow
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid
        return -1
