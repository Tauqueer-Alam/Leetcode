class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map <int,int> arr;

        for (int i=0;i<nums.size();i++){
            int first=nums[i];
            int second=target-first;

            if(arr.find(second)!=arr.end()){
                return{i,arr[second]};
            }

            arr[first]=i;
        }

        return {};

        
    }
};