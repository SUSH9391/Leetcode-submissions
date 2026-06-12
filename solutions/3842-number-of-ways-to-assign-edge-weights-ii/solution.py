from collections import defaultdict, deque

class Solution:
    def assignEdgeWeights(self, edges: list[list[int]], queries: list[list[int]]) -> list[int]:
        n = len(edges) + 1
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            
        # Binary Lifting Table
        LOG = 18  # 2^17 > 10^5
        up = [[-1] * LOG for _ in range(n + 1)]
        depth = [0] * (n + 1)
        
        # BFS to initialize depth and first ancestor
        q = deque([1])
        depth[1] = 0
        visited = {1}
        while q:
            u = q.popleft()
            for v in adj[u]:
                if v not in visited:
                    visited.add(v)
                    depth[v] = depth[u] + 1
                    up[v][0] = u
                    q.append(v)
        
        # Fill Binary Lifting Table
        for j in range(1, LOG):
            for i in range(1, n + 1):
                if up[i][j-1] != -1:
                    up[i][j] = up[up[i][j-1]][j-1]
        
        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            
            # 1. Bring u to the same depth as v
            diff = depth[u] - depth[v]
            for j in range(LOG):
                if (diff >> j) & 1:
                    u = up[u][j]
            
            if u == v:
                return u
            
            # 2. Lift both until they are just below LCA
            for j in range(LOG - 1, -1, -1):
                if up[u][j] != up[v][j]:
                    u = up[u][j]
                    v = up[v][j]
            return up[u][0]

        res = []
        MOD = 10**9 + 7
        for a, b in queries:
            if a == b:
                res.append(0)
            else:
                lca_node = get_lca(a, b)
                # Distance formula: depth[a] + depth[b] - 2 * depth[LCA]
                num_edges = depth[a] + depth[b] - 2 * depth[lca_node]
                res.append(pow(2, num_edges - 1, MOD))
                
        return res
