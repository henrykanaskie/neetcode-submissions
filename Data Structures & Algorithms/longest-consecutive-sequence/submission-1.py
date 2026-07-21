class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxlength = 0

        for num in numSet:
            if num -1 not in numSet:
                length = 1
                start = num + 1
                while start in numSet:
                    length += 1
                    start += 1
                maxlength = max(maxlength, length)

        return maxlength