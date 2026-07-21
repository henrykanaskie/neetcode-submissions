class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        output = []

        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))
        
        output.append(-heap[0][0])
        l, r = 1, k
        while r < len(nums):
            heapq.heappush(heap, (-nums[r], r))
            maximum, i = heap[0]
            if i >= l and i <= r:
                output.append(-maximum)
                l += 1
                r += 1
            else:
                heapq.heappop(heap)
        
        return output