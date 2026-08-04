class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #if some number has appered twice in the array return true without checking the other elements in the array 
        # also worst case id O(n) because if all the elemnts are distinct we are supposed to travesr through all the array elements 
        # space complexity is O(n) because we are using hasset to keep track of the elements 
        # so the idea is the numbers we see in array if present in hashset strightaway return true 
        hashset = set() #intialized a hasset
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n) # add the numbers from the array to hashset
        return False # when all the numbers are exausted from the array nums

