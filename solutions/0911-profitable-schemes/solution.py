class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10 **9 + 7
        dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for need, earn in zip(group, profit):
            for people in range(n, need -1 , -1):
                prev = dp[people - need]
                cur = dp[people]
                for p in range(minProfit + 1):
                    np = min(minProfit, p+earn)
                    cur[np] = (cur[np] + prev[p]) % MOD #this division is done at it prevents from increasing to very large number
        return sum(dp[i][minProfit] for i in range(n + 1)) %MOD
