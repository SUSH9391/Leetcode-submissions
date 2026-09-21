class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        seen = {}
        operations = 0
        for x in nums:
            if x > k:
                continue
            compliment = k - x
            if seen.get(compliment,0) > 0:
                seen[compliment]-= 1
                operations += 1
            else:
                seen[x] = seen.get(x, 0 ) + 1
        return operations
