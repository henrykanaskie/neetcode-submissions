class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(i, subset, summ):
            if summ == target:
                res.append(subset.copy())
                return
            if i >= len(nums) or summ > target:
                return
            
            subset.append(nums[i])
            dfs(i, subset, summ + nums[i])
            subset.pop()
            dfs(i + 1, subset, summ)

        dfs(0, [], 0)
        return res
            