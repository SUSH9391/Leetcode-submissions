class Solution {
public:

bool searchinrow(vector<vector<int>> matrix,int col, int row, int target){
    int st = 0, end = col-1;
    while (st<=end)
    {
        int mid = st + (end-st)/2;
        if(target == matrix[row][mid]){
            return true;
        }else if(target >= matrix[row][mid]){
            st = mid+1;
        }else{
            end= mid -1;
        }
    }
    return false;
}
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int row = matrix.size(), col = matrix[0].size();
    int strow = 0, endrow = row - 1;
    while (strow<=endrow)
    {
         int midrow = strow + (endrow - strow)/2;
        if (target >= matrix[midrow][0] && target <= matrix[midrow][col-1])
        {
           return searchinrow(matrix,col,midrow,target);
        }else if(target >= matrix[midrow][col-1]){
            strow = midrow +1;
        }else{
            endrow = midrow-1;
        }
        
    }
    return false;
    }
};
