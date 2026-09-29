class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # Optimization 1: A valid parenthesis string must have an even length
        if (m + n - 1) % 2 != 0:
            return False
            
        # Optimization 2: The path must start with an open bracket and end with a closed one
        if grid[0][0] == ')' or grid[m-1][n-1] == '(':
            return False
            
        # dp array stores a bitmask for each column in the current row.
        # The i-th bit represents whether a balance of i is possible.
        dp = [0] * n
        
        # Starting at (0, 0), the only possible balance is 1 (since it must be '(')
        dp[0] = 1 << 1  
        
        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    continue
                    
                # Combine valid balances from the cell above (r-1) and the cell to the left (c-1)
                mask = 0
                if r > 0:
                    mask |= dp[c]
                if c > 0:
                    mask |= dp[c-1]
                    
                # Shift the bitmask based on the current character
                if grid[r][c] == '(':
                    # An open bracket increases the balance (shift left)
                    dp[c] = mask << 1
                else:
                    # A close bracket decreases the balance (shift right)
                    # Note: Shifting right automatically drops negative balances!
                    dp[c] = mask >> 1
                    
        # Check if a balance of 0 (the 0-th bit) is possible at the target cell
        return (dp[n-1] & 1) != 0
