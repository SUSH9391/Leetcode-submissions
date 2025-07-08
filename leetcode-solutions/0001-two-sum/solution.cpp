class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        unordered_map<int, int> indexMap; // value -> index

    for (int i = 0; i < nums.size(); ++i) {
        int complement = target - nums[i];

        if (indexMap.count(complement)) {
            return {indexMap[complement], i}; // return original indices
        }

        indexMap[nums[i]] = i; // store current value and its index
    }

    return {};
    }
};
