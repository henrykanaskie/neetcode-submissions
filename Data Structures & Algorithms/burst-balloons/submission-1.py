class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        dp = {}
        nums = [1] + nums + [1]
        def pop(l, r):
            if l > r:
                return 0
            if (l,r) in dp:
                return dp[(l,r)]
        
            dp[(l,r)] = 0

            for i in range(l, r + 1):
                coins = nums[l-1] * nums[i] * nums[r + 1]
                coins += pop(l, i -1) + pop(i + 1, r)
                dp[(l, r)] = max(dp[(l,r)], coins)
            
            return dp[(l,r)]

        return pop(1, len(nums) - 2)