class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        n = len(intervals)
        starts = sorted(interval[0] for interval in intervals)
        ends = sorted(interval[1] for interval in intervals)
        non_intersecting = 0
        j = 0
        for start in starts:
            while j<n and ends[j] < start:
                j += 1
            non_intersecting += j
        total_pairs = n*(n-1) // 2
        return total_pairs - non_intersecting
