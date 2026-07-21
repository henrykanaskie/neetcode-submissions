class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxarea = 0
        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            maxarea = max(maxarea, area)
            if heights[l] >= heights[r]:
                r -= 1
            else:
                l += 1

        return maxarea