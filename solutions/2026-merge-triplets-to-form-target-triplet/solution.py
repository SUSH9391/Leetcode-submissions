class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # well be mantaining an set called good to judge if the len of the set is  == 3 since we sre comparing the triplets and triplets have a len of 3 
        good_triplets = set()
        for t in triplets:
            # [],[],[]
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue # skip that triplet
            for i,v in enumerate(t): 
                #we need the index and the value of induviduial triplet
                if v == target[i]:
                    good_triplets.add(i)
        return len(good_triplets) == 3
