class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        prefixes = set()
        
        # Step 1: Build the prefix set from arr1
        for val in arr1:
            val_str = str(val)
            for i in range(1, len(val_str) + 1):
                prefixes.add(val_str[:i])
                
        max_len = 0
        
        # Step 2 & 3: Check prefixes of arr2 against the set
        for val in arr2:
            val_str = str(val)
            for i in range(len(val_str), 0, -1):
                # Optimization: Break early if remaining prefix length can't beat current max
                if i <= max_len:
                    break
                    
                if val_str[:i] in prefixes:
                    max_len = max(max_len, i)
                    break  # Found the longest prefix for this specific number
                    
        return max_len
