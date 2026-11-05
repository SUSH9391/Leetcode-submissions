class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        count = 0
        
        for x in arr1:
            # Use binary search to find the insertion point of x in arr2
            import bisect
            idx = bisect.bisect_left(arr2, x)
            
            # Check the closest element to the left
            left_valid = (idx == 0 or abs(x - arr2[idx - 1]) > d)
            # Check the closest element to the right
            right_valid = (idx == len(arr2) or abs(x - arr2[idx]) > d)
            
            # If both closest neighbors are at a distance > d, keep it
            if left_valid and right_valid:
                count += 1
                
        return count
