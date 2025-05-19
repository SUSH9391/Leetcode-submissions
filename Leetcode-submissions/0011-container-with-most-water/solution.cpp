class Solution {
public:
    int maxArea(vector<int>& height) {
        int n=height.size();
        int lp = 0, rp=n-1, max_water=0, current_water=0;
        while(lp < rp){
            auto width = rp-lp;
            auto ht = min(height[lp],height[rp]);
            current_water=width*ht;
            max_water=max(max_water,current_water);
            height[lp]<height[rp]?lp++:rp--;
        }
        return max_water;
    }
};
