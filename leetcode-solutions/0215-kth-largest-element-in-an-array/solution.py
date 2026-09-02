import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Convert to finding the k-th smallest index (0-indexed)
        k = len(nums) - k 
        
        def quickSelect(arr, k_idx):
            # 1. Pick a random pivot
            pivot = random.choice(arr)
            
            # 2. Partition into 3 separate arrays
            left = [x for x in arr if x < pivot]
            mid = [x for x in arr if x == pivot]
            right = [x for x in arr if x > pivot]
            
            # 3. Figure out which array holds our target index
            if k_idx < len(left):
                # It's in the smaller numbers
                return quickSelect(left, k_idx)
                
            elif k_idx < len(left) + len(mid):
                # It's in the duplicates! We found it.
                return pivot
                
            else:
                # It's in the larger numbers. Adjust the index because 
                # we are throwing away the 'left' and 'mid' arrays.
                return quickSelect(right, k_idx - len(left) - len(mid))
                
        return quickSelect(nums, k)
