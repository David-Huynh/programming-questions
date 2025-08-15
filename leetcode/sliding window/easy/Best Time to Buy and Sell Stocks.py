class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for width in range(1,len(prices)):
            for shift in range(0,len(prices)-width):
                maxProfit = max(maxProfit, prices[shift+width] - prices[shift])

        return maxProfit
