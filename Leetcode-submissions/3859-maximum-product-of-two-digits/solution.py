class Solution:
    def maxProduct(self, n: int) -> int:
        d = [] # created a list to convert int to list so its iterable
        while n:
            d.append(n%10)
            n = n // 10
        d.sort()
        return d[-1] * d[-2]
