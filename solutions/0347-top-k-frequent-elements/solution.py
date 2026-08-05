class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} #create a hashmap so that when you iterate the nums array once and store their frequencies as the values {key : values}
        freq =[[] for i in range(len(nums) + 1)] #initialzes the list of list of numbers having frequ eg. if two numbers are equally frequent then they are stored as list in the corresponding index number
        res = [] # we are using a array to display the k no of frequent numbers and the space complxity is O(n)
        for n in nums:
            count[n] = 1 + count.get(n,0) # count.get(n) gets the value stored in key n if not present adds 0
        for key,val in count.items():
            freq[val].append(key)
        for i in range(len(freq) - 1, 0, -1): #start from the last since the last of the array denotes the maxinum frequency 
            for n in freq[i]:
                res.append(n)
                if len(res) == k :
                    return res

