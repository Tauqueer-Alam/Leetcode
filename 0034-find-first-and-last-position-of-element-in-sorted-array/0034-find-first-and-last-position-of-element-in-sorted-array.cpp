class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {

        auto firstPosition = [&]() {
            int left = 0;
            int right = nums.size() - 1;
            int ans = -1;

            while (left <= right) {
                int mid = left + (right - left) / 2;

                if (nums[mid] == target) {
                    ans = mid;
                    right = mid - 1;   // search left
                }
                else if (nums[mid] < target) {
                    left = mid + 1;
                }
                else {
                    right = mid - 1;
                }
            }

            return ans;
        };

        auto lastPosition = [&]() {
            int left = 0;
            int right = nums.size() - 1;
            int ans = -1;

            while (left <= right) {
                int mid = left + (right - left) / 2;

                if (nums[mid] == target) {
                    ans = mid;
                    left = mid + 1;    // search right
                }
                else if (nums[mid] < target) {
                    left = mid + 1;
                }
                else {
                    right = mid - 1;
                }
            }

            return ans;
        };

        return {firstPosition(), lastPosition()};
    }
};