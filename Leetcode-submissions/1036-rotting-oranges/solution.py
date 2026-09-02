from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        ROWS, COLS = len(grid), len(grid[0])
        time, fresh = 0, 0
        
        # Step 1: Count fresh oranges and push ALL initially rotten oranges to queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
                    
        # Edge case: If there are no fresh oranges to begin with, 0 minutes elapsed
        if fresh == 0:
            return 0
            
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        # Step 2: BFS Level-Order Traversal (each level = 1 minute)
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    # Out of bounds or not a fresh orange -> skip
                    if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or grid[nr][nc] != 1:
                        continue
                        
                    # Rot the fresh orange
                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr, nc))
                    
            # Completed one full wave of rotting across the grid
            time += 1
            
        return time if fresh == 0 else -1
