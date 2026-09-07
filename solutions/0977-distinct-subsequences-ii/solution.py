class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9+7
        dp = 1
        last = {}
        for c in s:
            new_dp = (dp*2 - last.get(c,0))
            last[c] = dp
            dp  = new_dp
        return (dp-1)%MOD
