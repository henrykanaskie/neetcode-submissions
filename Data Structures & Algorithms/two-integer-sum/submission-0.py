class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sets = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in sets:
                return [sets[diff], i]
            sets[num] = i
        