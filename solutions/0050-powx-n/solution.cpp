class Solution {
public:
    double myPow(double x, int n) {
        if (n == 0) return 1;
        if (x == 0) return 0;
        if (x == -1 && n % 2 == 0) return 1;
        if (x == -1 && n % 2 != 0) return -1;
        if (n == 1) return x;

        long binary_form = n;
        if (n < 0) {
            x = 1 / x;
            binary_form = -1L * binary_form;  // correct handling of INT_MIN
        }

        double ans = 1;
        while (binary_form > 0) {
            if (binary_form % 2 == 1) {
                ans *= x;
            }
            x *= x;
            binary_form /= 2;
        }
        return ans;
    }
};

