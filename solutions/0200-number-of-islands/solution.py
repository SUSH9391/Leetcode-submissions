class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        island = 0
        visit = set()
        
        def bfs(r, c):
            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))
            
            while q:
                # Use curr_r, curr_c so we don't overwrite the outer 'cols'
                curr_r, curr_c = q.popleft() 
                directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
                
                for dr, dc in directions:
                    new_r, new_c = curr_r + dr, curr_c + dc
                    
                    # Use new_r and new_c, and check against total 'rows' and 'cols'
                    if (0 <= new_r < rows and 
                        0 <= new_c < cols and 
                        grid[new_r][new_c] == "1" and # Fixed 'gird' to 'grid', and only visit "1"s
                        (new_r, new_c) not in visit):
                        
                        q.append((new_r, new_c))
                        visit.add((new_r, new_c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit: # Don't forget to check if it's already visited here!
                    bfs(r, c)
                    island += 1
                    
        return island
