class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * len(nums)
        post = [1] * len(nums)
        output = [0] * len(nums)
        for i in range(1, len(nums)):
            pre[i] = pre[i-1] * nums[i-1]
            post[-1-i] = post[-i] * nums[-i]
        for i in range(len(nums)):
            output[i] = pre[i] * post[i]

        return output
        