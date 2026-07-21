class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        length = len(piles)
        min_k = float('inf')
        while l <= r:
            m = (l + r) // 2
            t = 0
            for p in piles:
                t += (p + m - 1) // m
            if t <= h:
                min_k = min(m, min_k)
                r = m - 1
            else:
                l = m + 1
        
        return min_k
