
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()

        res = []
        cur = []

        def dfs(i, total):

            # Found a valid combination
            if total == 0:
                res.append(cur.copy())
                return

            # No more candidates
            if total < 0:
                return

            for j in range(i, len(candidates)):

                # Skip duplicates at the same recursion level
                if j > i and candidates[j] == candidates[j - 1]:
                    continue

                # Since array is sorted, everything after this
                # will also be too large
                if candidates[j] > total:
                    break

                # Choose
                cur.append(candidates[j])

                # Move forward so each element is used at most once
                dfs(j + 1, total - candidates[j])

                # Backtrack
                cur.pop()

        dfs(0, target)

        return res

