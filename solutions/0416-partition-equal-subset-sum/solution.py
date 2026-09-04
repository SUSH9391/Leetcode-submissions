class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums:
            return False
        if sum(nums) % 2:
            return False
        dp = set()
        dp.add(0)
        target = sum(nums) //2
        for i in range(len(nums)-1,-1,-1):
            newdp = set()
            for t in dp:
                if  (t) == target:
                    return True
                newdp.add(t+nums[i])
                newdp.add(t)
                dp = newdp
        return True if target in dp else False

        
