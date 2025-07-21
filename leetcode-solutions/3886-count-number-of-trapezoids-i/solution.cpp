class Solution {
    using ll = long long;
    const ll MOD = ll(1e9) + 7;
public:
    int countTrapezoids(vector<vector<int>>& points) {
        map<int, ll> mp;
        for(int i=0;i<int(points.size()); i++){
            mp[points[i][1]]++;
        }
        for(auto &[x,y]:mp){
            y=y*(y-1)/2; y%=MOD;
        }
        ll ans =0, tot=0;
        for(auto &[x,y] : mp){
            ans += y* tot; ans%=MOD;
            tot += y; tot%=MOD;
        }
        return ans;
    }
};
