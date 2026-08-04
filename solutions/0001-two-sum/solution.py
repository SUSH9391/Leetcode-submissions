class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #one way is to store the indices of the numbers in the hashmap and return them since we are fetching theindices from a hasmap and at the same iterating the complete array to store the indices to the hashmap we are running into 
        #time complexity of O(n)
        #space complexity O(n) since we are using extra memory of hashmap and storing the numbers: indices
        indices = {} # initalized an array to hold {number : indices}
        #since we need both the value and their indices we are gonna be using enumerate
        for i, n in enumerate(nums):
            #calculate how much more is needed to build the target number
            compliment = target - n
            if compliment in indices:
                return [indices[compliment], i] # we are supposed to return the array of the compliment number and the current number we are looking at which are capable to make a sum equal to target
            indices[n] = i #example {n-4: i-2}
        return []
