class Solution:
    def binsearch(self, l:int, r:int, nums: List[int], target: int) -> int:
        if l > r:
            return -1
        
        mid = l + (r - l) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.binsearch(mid+1, r, nums, target)
        else:
            return self.binsearch(l, mid-1, nums, target)
        
    def search(self, nums: List[int], target: int) -> int:
        return self.binsearch(0, len(nums) -1, nums, target)