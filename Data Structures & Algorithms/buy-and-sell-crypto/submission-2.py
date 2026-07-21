class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        l, r = 0, 0
        basis = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < basis:
                maxprofit = max(maxprofit, prices[i - 1] - basis)
                basis = prices[i]
            elif prices[i] < prices[i - 1]:
                maxprofit = max(maxprofit, prices[i - 1] - basis)
 
        maxprofit = max(maxprofit, prices[-1] - basis)
        return maxprofit

