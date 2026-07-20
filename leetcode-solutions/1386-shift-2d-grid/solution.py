class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total = m * n
        k = k % total
       
        if k == 0:
            return grid
        

        flat = [cell for row in grid for cell in row]
        
        shifted = flat[-k:] + flat[:-k]
        
        new_grid = []
        for i in range(0, total, n):
            new_grid.append(shifted[i : i + n])
            
        return new_grid
