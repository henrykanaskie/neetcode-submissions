class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def search(start, end):
            if start > end:
                return -1
            mid = start + int((end-start)//2)
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                return search(mid+1, end)
            else:
                return search(start, mid-1)

        return search(0, len(nums)-1)