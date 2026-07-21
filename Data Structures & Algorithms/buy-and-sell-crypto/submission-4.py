class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0
        max_profit = 0
        while r < len(prices) - 1:
            r += 1
            current_profit = prices[r] - prices[l]
            max_profit = max(max_profit, current_profit)
            if prices[l] > prices[r]:
                l = r
        
        return max_profit