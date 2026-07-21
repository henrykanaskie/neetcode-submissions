class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 1)


        for i in range(2, len(cost) + 1):
            onestep = dp[i - 1] + cost[i - 1]
            twostep = dp[i - 2] + cost[i - 2]
            mincost = min(onestep, twostep)
            dp[i] = mincost
        
        return dp[-1]