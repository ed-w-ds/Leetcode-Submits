# LINEAR TIME (O(n))

# better solution (more concise and less memory)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maximum = 0

        while l < r:
            area = (r - l) * min(height[r], height[l])
            maximum = max(maximum, area)
            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else:
                r -= 1
        return maximum

# first solution
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maximum, sum1 = 0, 0
        while l < r:
            sum1 = (r - l) * min(height[r], height[l])
            if sum1 > maximum:
                maximum = sum1
            if height[l] < height[r]:
                l += 1
            elif height[l] == height[r]:
                if r != len(height) - 1:
                    if height[l+1] < height[r + 1]:
                        l += 1
                    else:
                        r -= 1
                else:
                    r -= 1
            else: 
                r -= 1
        return maximum
