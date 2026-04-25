class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = [0] * (2*n)
        l1 = 0
        l2 = n

        for i in range(0, 2*n, 2):
            res[i] = nums[l1]
            res[i+1] = nums[l2]
            l1 += 1
            l2 += 1
        
        return res
