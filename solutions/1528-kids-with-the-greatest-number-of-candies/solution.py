class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_baseline = max(candies)
        return [candy + extraCandies >= max_baseline for candy in candies]
