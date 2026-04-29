class Solution:
    def rob(self, nums: List[int]) -> int:
        rob_first,rob_second = 0,0
        for n in nums:
            temp = max(n+rob_first,rob_second)
            rob_first = rob_second
            rob_second = temp
        return rob_second
        
