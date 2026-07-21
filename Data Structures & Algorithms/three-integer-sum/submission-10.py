class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        i = 0
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i -1]:
                continue
            target = -nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                twosum = nums[l] + nums[r]
                if twosum == target:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif twosum < target:
                    l += 1
                else:
                    r -= 1
                
            
        return res
