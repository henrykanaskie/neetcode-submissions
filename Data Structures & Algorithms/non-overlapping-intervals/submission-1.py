class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        numover = 0
        intervals.sort()
        lastend = intervals[0][1]
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            print (start, end, lastend )
            if start < lastend:
                numover += 1
                lastend = min(lastend, end) 
            else:
                lastend = end
        
        return numover