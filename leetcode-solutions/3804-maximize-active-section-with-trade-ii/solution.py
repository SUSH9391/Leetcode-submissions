import math
from typing import List


class SparseTable:

    def __init__(self, nums: List[int]):
        n = len(nums)
        if n == 0:
            return
        K = int(math.log2(n)) + 1 if n > 0 else 1
        self.st = [[0] * n for _ in range(K)]

        for j in range(n):
            self.st[0][j] = nums[j]

        for i in range(1, K):
            for j in range(n - (1 << i) + 1):
                self.st[i][j] = max(
                    self.st[i - 1][j], self.st[i - 1][j + (1 << (i - 1))]
                )

    def query(self, l: int, r: int) -> int:
        if l > r:
            return 0
        i = int(math.log2(r - l + 1))
        return max(self.st[i][l], self.st[i][r - (1 << i) + 1])


class Solution:

    def maxActiveSectionsAfterTrade(
        self, s: str, queries: List[List[int]]
    ) -> List[int]:
        n = len(s)
        ones = s.count("1")

        # Extract zero groups and assign each index to its group ID
        zero_groups = []  # stores (start_index, length)
        zero_group_index = [-1] * n

        for i, char in enumerate(s):
            if char == "0":
                if i > 0 and s[i - 1] == "0":
                    zero_groups[-1] = (
                        zero_groups[-1][0],
                        zero_groups[-1][1] + 1,
                    )
                else:
                    zero_groups.append((i, 1))
            zero_group_index[i] = len(zero_groups) - 1

        if not zero_groups:
            return [ones] * len(queries)

        # Precalculate merged lengths of fully internal adjacent zero blocks
        adjacent_sums = []
        for i in range(len(zero_groups) - 1):
            adjacent_sums.append(zero_groups[i][1] + zero_groups[i + 1][1])

        st = SparseTable(adjacent_sums)
        ans = []

        for l, r in queries:
            # Effective length of zero-block covering l
            left_len = -1
            if zero_group_index[l] != -1:
                g_start, g_len = zero_groups[zero_group_index[l]]
                left_len = g_len - (l - g_start)

            # Effective length of zero-block covering r
            right_len = -1
            if zero_group_index[r] != -1:
                g_start, _ = zero_groups[zero_group_index[r]]
                right_len = r - g_start + 1

            start_adj = zero_group_index[l] + 1
            end_adj = (
                zero_group_index[r]
                if s[r] == "1"
                else zero_group_index[r] - 1
            ) - 1

            active_sections = ones

            # Case 1: Both l and r fall in adjacent zero-blocks
            if (
                s[l] == "0"
                and s[r] == "0"
                and zero_group_index[l] + 1 == zero_group_index[r]
            ):
                active_sections = max(
                    active_sections, ones + left_len + right_len
                )

            # Case 2: Max adjacent block merge strictly between boundaries
            if start_adj <= end_adj:
                active_sections = max(
                    active_sections, ones + st.query(start_adj, end_adj)
                )

            # Case 3: Left partial block + full inner adjacent block
            if s[l] == "0" and zero_group_index[l] + 1 <= (
                zero_group_index[r] if s[r] == "1" else zero_group_index[r] - 1
            ):
                next_len = zero_groups[zero_group_index[l] + 1][1]
                active_sections = max(
                    active_sections, ones + left_len + next_len
                )

            # Case 4: Full inner adjacent block + Right partial block
            if s[r] == "0" and zero_group_index[l] < zero_group_index[r] - 1:
                prev_len = zero_groups[zero_group_index[r] - 1][1]
                active_sections = max(
                    active_sections, ones + right_len + prev_len
                )

            ans.append(active_sections)

        return ans
