# O(n) O(n)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonic decreasing stack
        result = [0] * len(temperatures)
        stack = [] # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackValue, stackIndex = stack.pop() # store the value and index of the element in the stack that you just popped
                result[stackIndex] = (i - stackIndex)
            stack.append([t, i])
        return result
