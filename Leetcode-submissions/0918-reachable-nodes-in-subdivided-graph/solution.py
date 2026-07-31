from typing import List
import heapq
class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v, c in edges:
            w = c+1
            graph[u].append((v,w))
            graph[v].append((u, w))
        dist = [float("inf")] * n
        dist[0] = 0
        pq = [(0, 0)]
        while pq:
            d, u = heapq.heappop(pq)
            if d != dist[u]:
                continue
            for v,w in graph[u]:
                nd = d+w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(pq, (nd,v))
        ans = sum(d <= maxMoves for d in dist)
        for u, v, c in edges:
            a= max(0, maxMoves - dist[u]) if dist[u] <= maxMoves else 0
            b = max(0, maxMoves-dist[v]) if dist[v] <= maxMoves else 0 
            ans += min(c, a+b)
        return ans
