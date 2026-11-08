class Solution:
    def countSuffix(self, nums: list[int], target: list[int]) -> int:
        n = len(nums)

        diff = defaultdict(int)
        nonzero = 0

        prefix_match = [True] * n
        for i in range(1, n):
            prefix_match[i] = prefix_match[i - 1] and nums[i - 1] == target[i - 1]

        ans = 0
        sorted_suffix = True

        for i in range(n - 1, -1, -1):

            for x, delta in ((nums[i], 1), (target[i], -1)):
                before = diff[x]
                diff[x] += delta
                after = diff[x]

                if before == 0 and after != 0:
                    nonzero += 1
                elif before != 0 and after == 0:
                    nonzero -= 1

            if i < n - 1 and target[i] < target[i + 1]:
                sorted_suffix = False

            if prefix_match[i] and nonzero == 0 and sorted_suffix:
                ans += 1

        return ans
