# T: O(n) Space: O(1) (no extra memory)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while numbers[l] + numbers[r] != target:
            sum1 = numbers[l] + numbers[r]
            if sum1 < target:
                l += 1
            else:
                r -= 1
        return [l+1, r+1]
