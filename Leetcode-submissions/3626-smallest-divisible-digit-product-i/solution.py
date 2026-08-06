class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def digit_product(num: int) -> int:
            prod = 1
            for digit in str(num):
                prod *= int(digit)
            return prod

        curr = n
        while True:
            if digit_product(curr) % t == 0:
                return curr
            curr += 1
