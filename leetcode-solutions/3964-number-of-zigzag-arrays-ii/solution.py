class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        def mul(a, b):
            n1, m1 = len(a), len(a[0])
            res = [[0] * m1 for _ in range(n1)]
            for i in range(n1):
                for j in range(m1):
                    for k in range(m1):
                        res[i][j] = (res[i][j] + a[i][k] * b[k][j]) % MOD
            return res
        def powMul(base, exp, res):
            while exp:
                if exp % 2 == 1: res = mul(res, base)
                base = mul(base, base)
                exp //= 2
            return res
        items = r - l +1
        size = 2 * items
        mat = [[0] * size for _ in range(size)]
        for i in range(items):
            for j in range(i): mat[i][j + items] = 1
            for j in range(i + 1, items): mat[i + items][j] = 1
        dp = [[1] * size]
        dp = powMul(mat, n-1, dp)
        return sum(dp[-1]) % MOD
