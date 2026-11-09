class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # Count servers in each row and column
        row_count = [sum(grid[i]) for i in range(m)]
        col_count = [sum(grid[i][j] for i in range(m)) for j in range(n)]
        
        communicating_servers = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    # A server communicates if there is another server in its row or column
                    if row_count[i] > 1 or col_count[j] > 1:
                        communicating_servers += 1
                        
        return communicating_servers
