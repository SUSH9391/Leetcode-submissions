class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        hash_set = set(nums)   #convert the list to set
        multiple  = k
        while multiple in hash_set:
            multiple += k
            #eg: k = 2 it is in num_set so now multipe becomes 2+ 2 =4 if 4 is in set then multiple becomes 4+2 = 6 if not in set will return that number because its the smallest number that isnt in set
        return multiple # k remains constant only multiple changes
