# time: O(n) | Space: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, maxProfit  = 0, 0
        for r in range(len(prices)):
            if prices[l] >= prices[r]:
                l = r
            else:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
        return maxProfit
