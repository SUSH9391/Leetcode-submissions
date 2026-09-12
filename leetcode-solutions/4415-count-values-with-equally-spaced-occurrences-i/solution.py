class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        pos = defaultdict(list)
        for i, x in enumerate(nums):
            pos[x].append(i)
        count = 0
        for indices in pos.values():
            if len(indices) == 3:
                i,j,k = indices
                if j-i == k-j:
                    count += 1
        return count
                
