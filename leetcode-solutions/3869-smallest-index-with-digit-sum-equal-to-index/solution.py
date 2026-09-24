class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        # example = [1,3,2] here at i =2 digit sum is equal to index and the only one among other 2 satifying this condition so output = 2
        #at [1,10,11] the digit sum is [1,1,2] both 1 and 2 satisfy but who os the smaller among them 
        for i, num in enumerate(nums):
            
            # Convert number to string, iterate through characters, and sum them as integers
            digit_sum = sum(int(digit) for digit in str(num))
            
            # Return the first matching index immediately
            if digit_sum == i:
                return i
                
        # If the loop completes without finding a match, return -1
        return -1

