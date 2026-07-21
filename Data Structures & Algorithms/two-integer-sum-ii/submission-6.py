class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            twosum = numbers[l] + numbers[r]
            if  twosum == target:
                return [l + 1,r + 1]
            if twosum > target:
                r -= 1
            if twosum < target:
                l += 1

        return 0 