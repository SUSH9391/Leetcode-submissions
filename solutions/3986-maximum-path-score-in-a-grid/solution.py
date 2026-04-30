class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        #m - row and n - columns
        m = len(grid)
        n = len(grid[0])
        #the right way to initalize a 3D dp array with uncomputed states are
        dp = [[[None for _ in range(k+1)] for _ in range(n)] for _ in range(m)]
        
        def helper(r: int, c: int, k: int) -> int:
            if r>=m or c>=n or k<0:
                return -1
            val = grid [r][c]
            anyCost = val >0

            if anyCost and k==0:
                return -1
            if r==m-1 and c==n-1:
                return val
            if dp[r][c][k] is not None:
                return dp[r][c][k]
            nextK = k
            if val > 0:
                nextK = k-1
            right = helper(r, c+1,  nextK)
            down = helper(r+1, c, nextK)
            if right == -1 and down == -1:
                dp[r][c][k] = -1
            else:
                dp[r][c][k] = val + max(right,down)

            return dp[r][c][k] 
        return helper(0,0,k)

            
