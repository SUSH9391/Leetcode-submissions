class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        index = 0 #we are starting from the 1st index
        total = 0 #having the count of total so that we never go out of gas travelling to an distance
        for g in range(len(gas)):
            total += (gas[g] - cost[g])
            if total < 0:
                total = 0 #reset total to 0 
                index = g + 1 # search the next index
        return index
