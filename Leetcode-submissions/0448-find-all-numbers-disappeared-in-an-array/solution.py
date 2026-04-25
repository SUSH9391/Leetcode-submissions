class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)+1
        seen = [False]*n
        for i in nums:
            seen[i] = True
        return [i for i in range(1,n) if not seen[i]]
