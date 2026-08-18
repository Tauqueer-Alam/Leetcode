class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int n=nums.size();
        unordered_map <int,int> freq;
        for(int i:nums){
            freq[i]++;
        }
        
        int maxfreq=0;
        int maxelement=0;
        for(auto p:freq){
            if (p.second>maxfreq){
                maxfreq=p.second;
                maxelement=p.first;
            }

        }

        return maxelement;

        
    }
};