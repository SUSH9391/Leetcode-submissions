class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unique_number = 0
        for n in nums:
            unique_number ^= n
        return unique_number
