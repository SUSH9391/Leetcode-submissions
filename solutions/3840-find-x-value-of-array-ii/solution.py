from typing import List

class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        # Allocate segment tree arrays (4 * n size is sufficient)
        tree_total = [0] * (4 * n)
        tree_cnt = [[0] * k for _ in range(4 * n)]
        
        def build(u: int, l: int, r: int):
            if l == r:
                val = nums[l] % k
                tree_total[u] = val
                tree_cnt[u][val] = 1
                return
            
            mid = (l + r) // 2
            left = 2 * u
            right = left + 1
            
            build(left, l, mid)
            build(right, mid + 1, r)
            
            # Merge logic for Build
            tree_total[u] = (tree_total[left] * tree_total[right]) % k
            
            tc_u = tree_cnt[u]
            tc_l = tree_cnt[left]
            tc_r = tree_cnt[right]
            ltot = tree_total[left]
            
            for i in range(k):
                tc_u[i] = tc_l[i]
            for i in range(k):
                if tc_r[i]:
                    tc_u[(ltot * i) % k] += tc_r[i]
                    
        def update(u: int, l: int, r: int, q_idx: int, q_val: int):
            if l == r:
                nv = q_val % k
                tree_total[u] = nv
                for i in range(k):
                    tree_cnt[u][i] = 0
                tree_cnt[u][nv] = 1
                return
            
            mid = (l + r) // 2
            left = 2 * u
            right = left + 1
            
            if q_idx <= mid:
                update(left, l, mid, q_idx, q_val)
            else:
                update(right, mid + 1, r, q_idx, q_val)
                
            # Merge logic for Update
            tree_total[u] = (tree_total[left] * tree_total[right]) % k
            tc_u = tree_cnt[u]
            tc_l = tree_cnt[left]
            tc_r = tree_cnt[right]
            ltot = tree_total[left]
            
            for i in range(k):
                tc_u[i] = tc_l[i]
            for i in range(k):
                if tc_r[i]:
                    tc_u[(ltot * i) % k] += tc_r[i]

        def query(u: int, l: int, r: int, ql: int, qr: int):
            # Perfect overlap
            if ql <= l and r <= qr:
                return tree_total[u], tree_cnt[u]
            
            mid = (l + r) // 2
            left = 2 * u
            right = left + 1
            
            if qr <= mid:
                return query(left, l, mid, ql, qr)
            elif ql > mid:
                return query(right, mid + 1, r, ql, qr)
            else:
                # Partial overlaps (merge results)
                ltot, lcnt = query(left, l, mid, ql, qr)
                rtot, rcnt = query(right, mid + 1, r, ql, qr)
                
                ntot = (ltot * rtot) % k
                ncnt = [0] * k
                
                for i in range(k):
                    ncnt[i] = lcnt[i]
                for i in range(k):
                    if rcnt[i]:
                        ncnt[(ltot * i) % k] += rcnt[i]
                        
                return ntot, ncnt

        # 1. Build initial Segment Tree
        build(1, 0, n - 1)
        
        ans = []
        # 2. Process queries
        for idx, val, start, x in queries:
            # Point Update
            update(1, 0, n - 1, idx, val)
            
            # Range Query from `start` to `n - 1`
            _, q_cnt = query(1, 0, n - 1, start, n - 1)
            ans.append(q_cnt[x])
            
        return ans
