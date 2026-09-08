class Solution:
    def countGoodRotations(self, nums: list[int]) -> int:
        # how to produce a cyclic rotation choosing a prefix of nums array whose kength is between 0 to n-1 where n-1 is include and moving the prefix to the end of array and preserving the order of othe elements we are supposed to return good cyclic rotaions the count of them a cyclic rotaion is good if n/2 from left  >  n/2 from right
        
        n = len(nums)
        k = n //2 # this is where the partition takes place
        left_sum = sum(nums[:k])
        right_sum = sum(nums[k:])
        good_rotations= 0 #since we are supposed to return the count of good rotaions 
        #now what are good rotaions whose left_Sum > right_sum
        if left_sum > right_sum :
            good_rotations+=1
        for i in range(1,n):
            popping_1st_ele = nums[i-1] #if i = 1 then pop 0th element
            appending_ele = nums[(i-1+k) % n]
            left_sum = left_sum - popping_1st_ele + appending_ele
            right_sum = right_sum - appending_ele + popping_1st_ele
            if left_sum > right_sum:
                good_rotations += 1
        return good_rotations
