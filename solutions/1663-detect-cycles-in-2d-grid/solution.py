class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        n, m = len(grid), len(grid[0])
        parent = list(range(n * m))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return True
            parent[ra] = rb
            return False

        for i in range(n):
            for j in range(m):
                if j + 1 < m and grid[i][j] == grid[i][j+1]:
                    if union(i*m+j, i*m+j+1):
                        return True
                if i + 1 < n and grid[i][j] == grid[i+1][j]:
                    if union(i*m+j, (i+1)*m+j):
                        return True
        return False
