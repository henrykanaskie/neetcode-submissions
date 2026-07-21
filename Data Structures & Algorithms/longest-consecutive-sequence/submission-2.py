class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0
        for i in range(len(nums)):
            if nums[i] - 1 not in numset:
                seqlen = 1
                j = 1
                while nums[i] + j in numset:
                    seqlen += 1
                    j += 1    
                longest = max(seqlen, longest)
                
        return longest
