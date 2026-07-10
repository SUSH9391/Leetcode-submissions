from typing import List
import bisect
from math import inf


class Solution:
    def pathExistenceQueries(
        self,
        n: int,
        nums: List[int],
        maxDiff: int,
        queries: List[List[int]]
    ) -> List[int]:

        # Sort values while keeping original indices
        arr = [(v, i) for i, v in enumerate(nums)]
        arr.sort()

        # Map original node index -> sorted index
        ntoi = {}
        for i, (_, node) in enumerate(arr):
            ntoi[node] = i

        # maxjumps[i] = furthest sorted index reachable in one jump
        maxjumps = [0] * n
        for i, (v, _) in enumerate(arr):
            nxt = bisect.bisect_left(arr, (v + maxDiff, inf)) - 1
            maxjumps[i] = nxt

        # Binary lifting table
        LOG = n.bit_length()
        up = [maxjumps]

        for _ in range(1, LOG):
            last = up[-1]
            up.append([last[last[i]] for i in range(n)])

        # Answer queries
        res = []

        for a, b in queries:
            a = ntoi[a]
            b = ntoi[b]

            if a == b:
                res.append(0)
                continue

            if a > b:
                a, b = b, a

            curr = a
            jumps = 0

            for k in range(LOG - 1, -1, -1):
                if up[k][curr] < b:
                    curr = up[k][curr]
                    jumps += 1 << k

            if maxjumps[curr] >= b:
                res.append(jumps + 1)
            else:
                res.append(-1)

        return res
