class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        common = min(need1, need2)
        
        # Cost for the common part covered simultaneously
        total_cost = common * min(costBoth, cost1 + cost2)
        
        # Remaining for need1
        rem1 = need1 - common
        total_cost += rem1 * min(cost1, costBoth)
        
        # Remaining for need2
        rem2 = need2 - common
        total_cost += rem2 * min(cost2, costBoth)
        
        return total_cost
