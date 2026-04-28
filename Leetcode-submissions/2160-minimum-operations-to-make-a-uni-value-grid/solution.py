class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # Flatten the 2D grid
        grid1d = [item for row in grid for item in row]
        
        # Every element must have the same remainder mod x
        # to be able to reach the same value using steps of size x.
        target_mod = grid1d[0] % x
        for val in grid1d:
            if val % x != target_mod:
                return -1
        grid1d.sort()
        median = grid1d[len(grid1d) // 2]
        total_ops = 0
        for val in grid1d:
            total_ops += abs(val - median) // x
            
        return total_ops

