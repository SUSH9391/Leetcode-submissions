class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = float("-inf")#we store the maximum area in this 
        l, r = 0 , len(height) - 1
        while l < r:
            area = (r-l) * min(height[l], height[r])
            res = max(res, area)
            if height[r]> height[l]:
                l += 1
            else:
                r -= 1
        return res
