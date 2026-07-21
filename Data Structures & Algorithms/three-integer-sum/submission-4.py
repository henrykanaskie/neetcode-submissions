class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l, r = 0, len(nums) - 1
        res = []
        nums.sort()
        while l < r:
            target = 0 - nums[l]
            m = l + 1
            while m < r:
                val = nums[m] + nums[r]
                if val == target:
                    if [nums[l], nums[m], nums[r]] not in res:
                        res.append([nums[l], nums[m], nums[r]])
                    m += 1
                    r -= 1
                elif val > target:
                    r -= 1
                else:
                    m += 1
            l += 1
            r = len(nums) - 1
        
        return res