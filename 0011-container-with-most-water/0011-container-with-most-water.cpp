class Solution {
public:
    int maxArea(vector<int>& height) {
        int n=height.size();
        int left=0;
        int right=n-1;
        int max_water=0;

        while(left<right){
            int width=right-left;
            int ht=min(height[right],height[left]);
            int area=width*ht;
            max_water=max(max_water,area);

            if(height[left]<height[right]){
                left++;
            }
            else {
                right--;
            
            }


        }

        return max_water;
        
    }
};