class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nSet = set(nums)
        longest = 0
        
        for n in nSet:
            if (n - 1) not in nSet:
                length = 1
                while (n + length) in nSet:
                    length += 1
                longest = max(length, longest)
                
        return longest
        
