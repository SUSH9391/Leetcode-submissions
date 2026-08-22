class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digit_sum = 0
        digit_prod = 1
        temp = n
        
        # Extract digits and calculate sum and product
        while temp > 0:
            digit = temp % 10
            digit_sum += digit
            digit_prod *= digit
            temp //= 10
            
        # Check if n is divisible by the sum of digit sum and digit product
        return n % (digit_sum + digit_prod) == 0
