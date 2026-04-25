
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_list = sorted(nums)
        count_map={}
        for i, num in enumerate(sorted_list):
            if num not in count_map:
                count_map[num] = i
        return [count_map[num] for num in nums]
