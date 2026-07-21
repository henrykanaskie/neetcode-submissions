class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 0 or len(nums) == 1:
            return nums
        ans = [0] * len(nums)
        enumerate(nums)
        pre = 1
        for i in range(len(nums)):
            ans[i] = pre
            pre = pre * nums[i]
        post = 1
        for i in range((len(nums)-1), -1, -1):
            ans[i] = ans[i] * post
            post = post * nums[i]
        
        
        
        
        return ans