class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #there is an array where the cost to climb the steps is given so the top step is actually after the final element in the array as you can see in this 1st example there are 3 costs which makes you genrally think therea are only 3 steps and the top step is the 3rd step but no the step is after n+1 and the cost to reach there is always 0
        cost.append(0) # hence we are appending the cost
        for i in range(len(cost) -3,-1,-1):
            cost[i] = min(cost[i]+cost[i+1],cost[i]+cost[i+2])
        return min(cost[0],cost[1])
