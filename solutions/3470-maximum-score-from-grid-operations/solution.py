class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        #given a nxn grid so take  n = len(grid) says all the grids are coloured white and we can select indices i,j and color black provided we can shade any column but in terms of row we can shade from top row to bottom row so shading is constrained in such a way that we can start shading fromtop row only
        n = len(grid)
        if n == 1: return 0

        dp= [[(0,0) for _ in range(n)] for _ in range(n+1)]

        for j in range(1,n):
            for i in range(n+1):
                dp0, dp1 = dp[i][j-1]
                prev = 0
                curr = sum(grid[p][j] for p in range(i))

                for k in range(n+1):
                    if k > 0 and k <= i: curr -= grid[k-1][j]
                    if k> i: prev += grid[k-1][j-1]

                    maxprev = max(dp1,dp0 + prev)
                    n0 = max(dp[k][j][0], maxprev)
                    n1 = max(dp[k][j][1], maxprev+curr)
                    dp[k][j]=(n0, n1)
        return max(dp[i][-1][1] for i in range(n+1))
