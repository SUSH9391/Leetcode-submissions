class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        # Pair each number with its original index and sort them by value
        sorted_nums = sorted([(nums[i], i) for i in range(n)])
        
        ans = [0] * n
        i = 0
        
        while i < n:
            j = i + 1
            # Find all elements that belong to the current connected component
            while j < n and sorted_nums[j][0] - sorted_nums[j - 1][0] <= limit:
                j += 1
            
            # Extract the original indices of this component and sort them
            indices = sorted([sorted_nums[k][1] for k in range(i, j)])
            
            # Place the sorted values back into the sorted original indices
            for k, index in enumerate(indices):
                ans[index] = sorted_nums[i + k][0]
                
            # Move to the next component
            i = j
            
        return ans
