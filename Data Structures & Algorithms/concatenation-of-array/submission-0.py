class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * (len(nums) * 2)
        for i in range(len(ans)):
            index = (i % len(nums))
            ans[i] = nums[index] if i >= len(nums) else nums[i]

        return ans