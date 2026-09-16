import sys
from typing import List

# Increase recursion depth just in case the tree is a straight line of 500 nodes
sys.setrecursionlimit(2000)

class Solution:
    def goodSubtreeSum(self, vals: List[int], par: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(vals)
        
        # 1. Build the tree (Adjacency list of children)
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[par[i]].append(i)
            
        # 2. Precompute the bitmask for each node's value
        # If a value has duplicate digits, we give it a mask of -1
        def get_mask(val):
            mask = 0
            for ch in str(val):
                digit = int(ch)
                if mask & (1 << digit):
                    return -1 # Duplicate digit found
                mask |= (1 << digit)
            return mask
            
        masks = [get_mask(v) for v in vals]
        max_score = [0] * n
        
        # 3. Tree DP using Post-Order Traversal (DFS)
        def dfs(u):
            # dp maps: bitmask -> max_score
            # We always start with the empty set (mask 0, score 0)
            dp = {0: 0}
            
            # If the current node itself is valid, add it to our starting combinations
            if masks[u] != -1:
                dp[masks[u]] = vals[u]
                
            # Process and merge each child
            for v in adj[u]:
                child_dp = dfs(v)
                new_dp = {}
                
                # Merge current u's combinations with v's combinations
                # Using .items() ensures we ONLY iterate over reachable masks!
                for mask_u, score_u in dp.items():
                    for mask_v, score_v in child_dp.items():
                        # If the subsets share NO digits
                        if (mask_u & mask_v) == 0:
                            combined_mask = mask_u | mask_v
                            combined_score = score_u + score_v
                            
                            # Keep the maximum score for this combined mask
                            if new_dp.get(combined_mask, -1) < combined_score:
                                new_dp[combined_mask] = combined_score
                                
                # Move to the newly merged state before processing the next child
                dp = new_dp
                
            # The max score for this subtree is simply the maximum value in our dp dictionary
            max_score[u] = max(dp.values())
            return dp
            
        # Kick off DFS from the root (0)
        dfs(0)
        
        # Return the sum of all subtree maximums, modulo 10^9 + 7
        return sum(max_score) % MOD
