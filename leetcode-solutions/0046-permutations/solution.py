class Solution:

    def permute(self, nums:List[int])->List[List[int]]:
        if not nums:
            return
        res = []
        used = [False] * len(nums)
        

        def dfs(subset):
            if len(subset) == len(nums):
                res.append(subset[:])
                return

            for i in range(len(nums)):

                if used[i]:
                    continue

                subset.append(nums[i])
                used[i] = True

                dfs(subset)

                used[i] = False
                subset.pop()

        dfs([])

        return res
