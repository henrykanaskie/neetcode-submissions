class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        l, r = 0, 0
        max_profit = 0
        while r < len(prices) - 1:
            r += 1
            current_profit = prices[r] - prices[l]
            max_profit = max(max_profit, current_profit)
            while prices[l] > prices[r]:
                l += 1
        
        return max_profit