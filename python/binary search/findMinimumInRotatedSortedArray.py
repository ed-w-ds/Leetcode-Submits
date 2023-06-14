# O(logn)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # res can be any value from nums list
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            # if first value in nums is lower than last value, it means the array is already sorted
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            mid = (l + r) // 2 
            res = min(res, nums[mid])
            # means infliction point is not between l and mid therefore it is on the right side of the array / window
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        return res


