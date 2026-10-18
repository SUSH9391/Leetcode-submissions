class Solution:
    def minDeletions(self, nums: list[int]) -> int:
        #here we can use dynamic programming approch
        deletions = 0
        last_kept = -1
        for num in nums:
            if num == last_kept:
                deletions += 1
            else:
                last_kept = num
        return deletions
