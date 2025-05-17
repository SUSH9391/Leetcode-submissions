class Solution {
public:
    int majorityElement(vector<int>& nums) {
    //     sort(nums.begin(),nums.end()); //sorts the array
    //     //to calculate fequency
    //     int freq = 1, ans = nums[0];
    //     for (int i=1; i<nums.size(); i++){
    //         if(nums[i]==nums[i-1]){
    //             freq++;
    //         }
    //         else{
    //             freq= 1;
    //             ans = nums[i];
    //         }
    //        if(freq > nums.size()/2){
    //          return ans;
    //        }
    //     }
    //     return ans;
    // }//O(NLOGN)N
    int fequ= 0, ans = nums[0];
    for(int i=0;i<nums.size();i++){
        if (fequ == 0){
            ans = nums[i];
        }
        if(ans == nums[i]){
            fequ++;
        }
        else{
            fequ--;
        }
    }
    int count =0;
    for (int val: nums){
        if(val == ans){
            count++;
        }
    }
    if (count>nums.size()/2) {
        return ans;
        }
    else{-1;}
    return ans;
    }

};
