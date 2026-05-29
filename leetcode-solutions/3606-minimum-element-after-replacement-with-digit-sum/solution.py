class Solution:
    def minElement(self, nums: List[int]) -> int:
        def get_digit_sum(n):
            total = 0
            while n > 0:
                total += n % 10
                n //= 10
            return total
        digit_sums = [get_digit_sum(num) for num in nums]
        return min(digit_sums)
