class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        num_i = num_j = float('inf')
        for n in nums:
            if n<=num_i:
                num_i = n
            elif n<=num_j:
                num_j = n
            else:
                return True
        return False
