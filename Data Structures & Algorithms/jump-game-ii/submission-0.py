class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        if nums[0] == 0:
            return -1
        l, r = 0, 0
        res = 0
        maxrange = 0
        while r < len(nums) - 1:
            for i in range(l, r + 1):
                cur = nums[i] + i
                maxrange = max(cur, maxrange)
            
            l = r + 1
            r = maxrange
            
            res += 1

        return res