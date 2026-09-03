class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        minHeap = [(grid[0][0], 0, 0)]
        visit =set([(0,0)])
        directions = [[0,1],[-1,0],[0,-1],[1,0]]
        while minHeap:
            max_elevation, r, c = heapq.heappop(minHeap)
            if r == n-1 and c == n-1:
                return max_elevation
            for dr, dc in directions:
                nr,nc = dr+r, dc+c
                if 0<=nr<n and 0<=nc<n and (nr,nc) not in visit:
                    visit.add((nr,nc))
                    new_elevation = max(max_elevation,grid[nr][nc])
                    heapq.heappush(minHeap,(new_elevation,nr,nc))
        return 0
            
