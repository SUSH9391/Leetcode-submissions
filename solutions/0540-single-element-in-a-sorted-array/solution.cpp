class Solution {
public:
    int singleNonDuplicate(vector<int>& a) {
        int n = a.size();
        int st=0,end=n-1;
        if(n==1) return a[0];
        while(st<=end){
            int mid = st+(end-st)/2;
            if(mid == 0 && a[mid] != a[mid+1]){
                return a[mid];
            }
            if(mid == n-1 && a[mid] != a[mid-2]){
                return a[mid];
            }
            if(a[mid-1] != a[mid] && a[mid]!= a[mid+1])
                return a[mid];
            if(mid % 2 == 0){
                if(a[mid-1] == a[mid]){
                    end = mid-1;
                }else{
                    st = mid+1;
                }
            }else{
                if(a[mid-1] == a[mid]){
                    st = mid+1;
                }else{
                    end = mid-1;
                }
            }
            

            }
            return -1;
        }   
    
};
