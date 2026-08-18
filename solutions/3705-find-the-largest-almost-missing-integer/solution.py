class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        # Case 1: The window size is the entire array.
        # There is only 1 subarray, so every element appears in exactly 1 subarray.
        if k == len(nums):
            return max(nums)
        
        # Case 2: The window size is 1.
        # We need the absolute largest number that appears exactly once in the whole array.
        if k == 1:
            largest = -1
            for num in nums:
                if nums.count(num) == 1:
                    largest = max(largest, num)
            return largest
        
        # Case 3: The window size is between 1 and len(nums).
        # Any middle element will be in multiple overlapping windows.
        # Only the very first and very last elements are candidates.
        largest = -1
        
        if nums.count(nums[0]) == 1:
            largest = max(largest, nums[0])
            
        if nums.count(nums[-1]) == 1:
            largest = max(largest, nums[-1])
            
        return largest
