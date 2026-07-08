class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)

        ps = [0] * n
        pc = [0] * n
        px = [0] * n

        d = int(s[0])
        ps[0] = d
        pc[0] = 1 if d != 0 else 0
        px[0] = d if d != 0 else 0
        for i in range(1, n):
            d = int(s[i])
            ps[i] = (ps[i - 1] + d) % MOD
            pc[i] = pc[i - 1] + (1 if d != 0 else 0)
            if d != 0: px[i] = (px[i - 1] * 10 + d) % MOD
            else: px[i] = px[i - 1]
        res = []
        for l, r in queries:
            sm = ps[r] - (ps[l- 1] if l -1 >= 0 else 0)
            non_zero_digits = pc[r] - (pc[l - 1] if l - 1 >= 0 else 0)
            x =(px[r] - (px[l - 1] * pow(10, non_zero_digits, MOD) if l - 1 >= 0 else 0)) % MOD
            res.append((x * sm) % MOD)
        return res

