class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1, nums[0]]
        postfix = [1, nums[-1]]

        for i in range(2, len(nums)):
            prefix.append(prefix[i-1] * nums[i-1])

        for i in range(2, len(nums)):
            postfix.append(postfix[i - 1] * nums[- i])
        
        res = []
        for i in range(len(nums)):
            res.append(prefix[i] * postfix[-1-i])
        return res