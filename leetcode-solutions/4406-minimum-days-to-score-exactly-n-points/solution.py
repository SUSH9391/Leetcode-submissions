class Solution:
    def minDays(self, n: int) -> int:
        days = 0
        points = 0
        while points < n:
            days+= 1
            points += days
        if points == n:
            return days
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        for j in range(1,n+1):
            k = 1
            while k * (k+1) // 2 <= j:
                score = k * (k+1) // 2
                cost = k if dp[j-score] == 0 else k + 1
                dp[j] = min(dp[j],dp[j-score]+cost)
                k += 1
        return dp[n]
        
