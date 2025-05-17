class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int max_sum = INT_MIN;
        int curr_ele=0;
        for(int val: nums){
            curr_ele += val;
            max_sum = max(curr_ele,max_sum);
            if(curr_ele<0){
                curr_ele = 0;
            }
        }
        return max_sum;
    }
};
