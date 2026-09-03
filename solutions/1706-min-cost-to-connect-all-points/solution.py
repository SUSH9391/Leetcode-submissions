class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = collections.defaultdict(list)
        for i in range(len(points)):
            for j in range(len(points)):
                x1,y1 = points[i]
                x2,y2 = points[j]
                weight = abs(x1-x2) + abs(y1-y2)
                adj[i].append((weight, j))
                adj[j].append((weight,i))
        #prims algo
        #we are taking minimum cost we are not minimizing so we make minCost = 0
        minCost = 0
        visit = set()
        #set minHeap as [weight,node_index]
        minHeap = [(0,0)]
        while len(visit) < n: # before all the points are visited 
            weight, u = heapq.heappop(minHeap)
            if u in visit:
                continue
            visit.add(u)
            minCost  += weight  # the min cost to visit the node u is weight + mincost so far
            for neiweight , v in adj[u]:
                if v not in visit:
                    heapq.heappush(minHeap, (neiweight, v))
        return minCost
