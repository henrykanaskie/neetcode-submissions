class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i in range(len(nums)):
            visited[nums[i]] = i
        for i,num in enumerate(nums):
            val = target - num
            if val in nums:
                if i != visited[val]:
                    return [i, visited[val]]
            
        return []

       
        