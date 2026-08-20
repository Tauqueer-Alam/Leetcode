class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());

        set<vector<int>> set1;

        for (int i = 0; i < nums.size() - 2; i++) {
            int left = i + 1;
            int right = nums.size() - 1;

            while (left < right) {
                int total = nums[i] + nums[left] + nums[right];

                if (total == 0) {
                    vector<int> triplet = {
                        nums[i],
                        nums[left],
                        nums[right]
                    };

                    set1.insert(triplet);

                    left++;
                    right--;
                }
                else if (total < 0) {
                    left++;
                }
                else {
                    right--;
                }
            }
        }

        vector<vector<int>> result(set1.begin(), set1.end());

        return result;
    }
};