from typing import List

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        if n <= 1:
            return 0
        
        # Step 1: Prefix sum to quickly calculate subarray sums
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + stoneValue[i]
            
        # dp[i][j] stores the max score Alice can get from stones i to j
        dp = [[0] * n for _ in range(n)]
        
        # max_l[i][j] stores max(dp[i][k] + sum(i...k)) for k in range i to j
        max_l = [[0] * n for _ in range(n)]
        
        # max_r[i][j] stores max(dp[k][j] + sum(k...j)) for k in range i to j
        max_r = [[0] * n for _ in range(n)]
        
        # Initialize base cases (range of length 1)
        for i in range(n):
            max_l[i][i] = stoneValue[i]
            max_r[i][i] = stoneValue[i]
            
        # Step 2: Bottom-Up DP
        # We loop i backwards and j forwards to ensure subproblems are solved first
        for i in range(n - 1, -1, -1):
            ip = i + 1 # ip acts as our two-pointer to track the split point
            for j in range(i + 1, n):
                # The target sum for splitting the row perfectly in half
                mid_val = (prefix[i] + prefix[j+1]) / 2.0
                
                # Advance pointer until the left partition's sum exceeds the mid_val
                while ip <= j and prefix[ip] <= mid_val:
                    ip += 1
                
                # idx is the largest index k where left_sum <= right_sum
                idx = ip - 2
                
                res = 0
                
                # Case 1 & 2: left_sum <= right_sum
                if idx >= i:
                    res = max(res, max_l[i][idx])
                    # Handle a perfect tie (left_sum == right_sum)
                    if prefix[idx+1] * 2 == prefix[i] + prefix[j+1]:
                        res = max(res, max_r[idx+1][j])
                    # If it's not a tie, Bob will force Alice to the right side if she splits at k > idx
                    elif idx + 2 <= j:
                        res = max(res, max_r[idx+2][j])
                
                # Case 3: No valid split where left_sum <= right_sum
                else:
                    res = max(res, max_r[i+1][j])
                    
                dp[i][j] = res
                
                # Step 3: Update our max_l and max_r lookups for future expansions
                curr_sum = prefix[j+1] - prefix[i]
                max_l[i][j] = max(max_l[i][j-1], res + curr_sum)
                max_r[i][j] = max(max_r[i+1][j], res + curr_sum)
                
        return dp[0][n-1]
