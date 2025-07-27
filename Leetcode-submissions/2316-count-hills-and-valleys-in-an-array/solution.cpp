#include <vector>
using namespace std;

class Solution {
public:
    int countHillValley(vector<int>& nums) {
        int ans = 0;
        int left = nums[0];
        for (int i = 1; i + 1 < nums.size(); ++i) {
            if ((left < nums[i] && nums[i] > nums[i + 1]) || // hill
                (left > nums[i] && nums[i] < nums[i + 1])) { // valley
                ++ans;
                left = nums[i]; // move the left pointer to the new position
            }
            // Only update left if nums[i] != nums[i+1]
            if (nums[i] != nums[i + 1])
                left = nums[i];
        }
        return ans;
    }
};

