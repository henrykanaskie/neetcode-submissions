class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxW = 0
        l, r = 0, len(heights) - 1
        while l < r:
            dist = r - l
            vol = dist * min(heights[l], heights[r])
            if heights[l] >= heights[r]:
                r -= 1
            else:
                l += 1
            maxW = max(maxW, vol)

        return maxW