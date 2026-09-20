class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        n = len(intervals)
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                start1,end1 = intervals[i]
                start2, end2 = intervals[j]
                if max(start1,start2) <= min(end1,end2):
                    count += 1
        return count
