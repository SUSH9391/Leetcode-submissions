class Solution {
public:
    void nextPermutation(vector<int>& A) {
        int pivot = -1, n = A.size();

        // Step 1: Find the pivot
        for (int i = n - 2; i >= 0; i--) {
            if (A[i] < A[i + 1]) {
                pivot = i;
                break;
            }
        }

        // Step 2: If no pivot, reverse the array
        if (pivot == -1) {
            reverse(A.begin(), A.end());
            return;
        }

        // Step 3: Find the next greater element to swap with pivot
        for (int i = n - 1; i > pivot; i--) {
            if (A[i] > A[pivot]) {
                swap(A[i], A[pivot]);
                break;
            }
        }

        // Step 4: Reverse the suffix
        reverse(A.begin() + pivot + 1, A.end());
    }
};

