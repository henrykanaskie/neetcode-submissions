class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        maxarea = -1

        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                ind, val = stack.pop()
                diff = i - ind
                maxarea = max(maxarea, (val * diff))
                start = ind
            
            stack.append((start, h))
        for i, h in stack:
            area = h * (n - i)
            maxarea = max(maxarea, area)
        
        return maxarea
