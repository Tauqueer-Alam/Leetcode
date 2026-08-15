#include <algorithm>
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int n=nums.size();
        for(int i=0;i<n;i++){
            int result=count(nums.begin(),nums.end(),nums[i]);
            if (result==1){
                return nums[i];
            }
        }
        return 0;
        
    }
};