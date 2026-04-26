from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        dravonikel = nums
        total = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                total += nums[i - 1] - nums[i]
        return total
