class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        n, m = len(grid), len(grid[0])
        dist = [[inf] * m for _ in range(n)]
        dist[0][0] = grid[0][0]
        q = deque()
        q.append((grid[0][0], 0, 0))
        
        while q:
            c, i, j = q.popleft()
            for ni, nj in((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if ni < 0 or ni >= n or nj < 0 or nj >= m: continue
                nc = c + grid[ni][nj]
                if nc <dist[ni][nj]:
                    dist[ni][nj] = nc
                    if nc == c: q.appendleft((nc, ni, nj))
                    else: q.append((nc, ni, nj))
        return dist[-1][-1] < health
