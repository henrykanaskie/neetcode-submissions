class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)
        
        while len(heap) > 1:
            y, x = -1 * heapq.heappop(heap), -1 * heapq.heappop(heap)

            if x == y:
                continue
            else:
                heapq.heappush(heap, -1 * (y - x))
        
        return -heap[0] if heap else 0
