class Solution {
public:
    
    long double areaBelow(long double y, vector<vector<int>>& squares) {
        long double below = 0.0L;

        for (auto &sq : squares) {
            long double Y = (long double)sq[1];   
            long double side = (long double)sq[2];
            long double top = Y + side;

            if (y <= Y) {
                
                continue;
            } 
            else if (y >= top) {
                
                below += side * side;
            } 
            else {
                
                below += (y - Y) * side;
            }
        }
        return below;
    }

    double separateSquares(vector<vector<int>>& squares) {
        long double totalArea = 0.0L;
        long double low = 1e18L, high = -1e18L;

        for (auto &sq : squares) {
            long double Y = (long double)sq[1];
            long double side = (long double)sq[2];

            totalArea += side * side;

            low = min(low, Y);          
            high = max(high, Y + side); 
        }

        long double target = totalArea / 2.0L;

       
        for (int it = 0; it < 80; it++) {  
            long double mid = (low + high) / 2.0L;
            if (areaBelow(mid, squares) < target) {
                low = mid;  
            } else {
                high = mid;  
            }
        }

        return (double)high;
    }
};

