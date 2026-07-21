class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergesort(l):
            if len(l) <= 1:
                return l
            mid = len(l) // 2
            left = mergesort(l[:mid])
            right = mergesort(l[mid:])
            return merge(left, right)
        
        def merge(left, right):
            res = []
            i = j = 0

            while i <len(left) and j < len(right):
                if left[i] <= right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1
            res.extend(left[i:])
            res.extend(right[j:])
            return res
        
        return mergesort(nums)