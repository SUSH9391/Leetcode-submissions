class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        def check(limit):
            h = [(0, 0)]
            dist = [k+1] * n
            dist[0] = 0

            while h:
                w, node = heapq.heappop(h)
                if node == n - 1: return True
                if w > dist[node]: continue
                for nw, nei in adj[node]:
                    if nw < limit: continue
                    acc = w + nw
                    if acc < dist[nei]:
                        dist[nei] = acc
                        heapq.heappush(h, (acc, nei))
            return False
        l = inf
        r = 0
        n = len(online)

        adj = defaultdict(list)
        for a, b , w in edges:
            if not online[a] or not online[b]:continue
            adj[a].append((w, b))
            l = min(l, w)
            r = max(r,w)
        res = -1
        while l <= r:
            mid = l +(r - l) // 2
            if check(mid):
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        return res
