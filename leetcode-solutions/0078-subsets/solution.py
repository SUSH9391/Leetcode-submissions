class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #the numbers can be negative as well as 
        if not nums:
            return nums
        res = []
        
        def dfs(i,subset):
            if i >= len(nums): #if [1] len = 1 i = 0 > 1
                res.append(subset[:])
                return
            subset.append(nums[i])
            dfs(i+1,subset)
            subset.pop()
            dfs(i+1,subset)
        dfs(0, [])
        return res
