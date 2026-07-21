class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        maxprod, minprod = 1, 1

        for num in nums:
            temp = maxprod * num
            maxprod = max(num * maxprod, num * minprod, num)
            minprod = min(temp, num * minprod, num)
            res = max(res, maxprod)
        return res