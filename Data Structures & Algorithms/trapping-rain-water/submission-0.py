class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l, r = 0, len(height)-1
        maxl, maxr = height[0], height[r]
        ans = 0
        while l < r:
            if maxl > maxr:
                
                val = maxr - height[r] 
                if val > 0:
                    ans += val
                else:
                    ans += 0
                r -= 1
                if height[r] > maxr:
                    maxr = height[r]
            else:

                val = maxl - height[l] 
                if val > 0:
                    ans += val
                else:
                    ans += 0
                l += 1
                if height[l] > maxl:
                    maxl = height[l]
        return ans

                
        