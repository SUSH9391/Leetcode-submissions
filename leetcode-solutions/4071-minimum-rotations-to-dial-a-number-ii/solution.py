class Solution:
    def minRotations(self, n: int, s: str) -> int:
        # Convert string to list of integers for faster lookup
        nums = [int(char) for char in s]
        
        def dist(a: int, b: int) -> int:
            diff = abs(a - b)
            return min(diff, 10 - diff)
            
        # Step 1: Calculate the base cost without any reversals
        total_cost = dist(0, nums[0])
        for i in range(1, n):
            total_cost += dist(nums[i-1], nums[i])
            
        min_cost = total_cost
        
        # Step 2: Try reversing the suffix starting at k = 0 (the entire string)
        new_cost_0 = total_cost - dist(0, nums[0]) + dist(0, nums[-1])
        min_cost = min(min_cost, new_cost_0)
        
        # Step 3: Try reversing the suffix starting at k > 0
        for k in range(1, n):
            # We subtract the old link cost (s[k-1] to s[k]) 
            # and add the new link cost (s[k-1] to s[n-1])
            new_cost = total_cost - dist(nums[k-1], nums[k]) + dist(nums[k-1], nums[-1])
            min_cost = min(min_cost, new_cost)
            
        return min_cost
