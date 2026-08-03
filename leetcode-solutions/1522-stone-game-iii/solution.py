class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        # dp[i] represents the maximum score difference the current player
        # can get starting from stone i to the end.
        dp = [0] * (n + 1)
        
        # Iterate backwards from the last stone to the first
        for i in range(n - 1, -1, -1):
            max_val = -float('inf')
            current_sum = 0
            
            # A player can take 1, 2, or 3 stones
            for k in range(1, 4):
                if i + k - 1 < n:
                    current_sum += stoneValue[i + k - 1]
                    max_val = max(max_val, current_sum - dp[i + k])
            
            dp[i] = max_val
            
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"
