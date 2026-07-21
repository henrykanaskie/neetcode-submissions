class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        total_prod = 1
        for i in range(len(nums)):
            if nums[i] != 0:
                total_prod *= nums[i]
        zero_count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count += 1
                output[i] += total_prod 
                if zero_count > 1:
                    return [0] * len(nums)
            elif 0 in nums:
                output[i] = 0
            else:
                output[i] += total_prod // nums[i]
            
            

        return output