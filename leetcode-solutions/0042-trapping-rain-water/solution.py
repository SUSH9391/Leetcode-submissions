class Solution:
    def trap(self, height: List[int]) -> int:
        #assign two pointers and lets compare the heights of both sides coz to trap water we need both ends
        l , r = 0, len(height) - 1
        leftMax = height[l]
         # maximum height uptill lift pointer's reach
        
        rightMax = height[r]# maximum height uptill right pointers reach
        res = 0 #since we are suppoed to output the sum of all the water that is trapped in this elevation map

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l]) #height[l] is the current height
                res += leftMax - height[l]
            else: 
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res

