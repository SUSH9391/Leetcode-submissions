import bisect
from typing import List

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        
        # Store original intervals with their original index
        arr = []
        for i in range(n):
            arr.append((intervals[i][0], intervals[i][1], intervals[i][2], i))
        
        # Sort by right endpoint to facilitate non-overlapping prefix searches
        arr.sort(key=lambda x: x[1])
        
        # Extract just the right boundaries for binary searching
        R_vals = [x[1] for x in arr]
        
        # dp[c][i] stores (max_score, lexicographically_smallest_indices_list)
        # c goes up to 4 (since we can choose at most 4 intervals)
        # i goes up to n (1-indexed for DP prefix ease)
        dp = [[(0, []) for _ in range(n + 1)] for _ in range(5)]
        
        for c in range(1, 5):
            for i in range(1, n + 1):
                l, r, w, idx = arr[i - 1]
                
                # Find the rightmost interval that ends strictly before current interval starts.
                # bisect_left gives us the number of intervals where R_vals < l,
                # which aligns perfectly with our 1-indexed DP array representation.
                j = bisect.bisect_left(R_vals, l)
                
                prev_score, prev_indices = dp[c - 1][j]
                
                # Candidate 1: Take the current interval
                cand1_score = prev_score + w
                cand1_indices = sorted(prev_indices + [idx])
                
                # Candidate 2: Skip the current interval
                cand2_score, cand2_indices = dp[c][i - 1]
                
                # Compare and update state:
                # 1. Higher score always wins.
                # 2. If scores are tied, the lexicographically smaller indices list wins.
                if cand1_score > cand2_score:
                    dp[c][i] = (cand1_score, cand1_indices)
                elif cand1_score < cand2_score:
                    dp[c][i] = (cand2_score, cand2_indices)
                else:
                    if cand1_indices < cand2_indices:
                        dp[c][i] = (cand1_score, cand1_indices)
                    else:
                        dp[c][i] = (cand2_score, cand2_indices)
                        
        # The answer for up to 4 intervals considering all n items
        return dp[4][n][1]
