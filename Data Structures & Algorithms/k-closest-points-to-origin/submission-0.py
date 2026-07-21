class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for p in points:
            distance = self.euclid(p)
            heapq.heappush(heap,(distance, p))
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res

    def euclid(self, point:int):
        return math.sqrt(point[0]**2 + point[1] ** 2)