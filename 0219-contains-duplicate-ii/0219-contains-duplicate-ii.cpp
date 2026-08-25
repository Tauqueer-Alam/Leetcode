class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_set<int> window;

        for (int i = 0; i < nums.size(); i++) {

            // If duplicate exists inside current window
            if (window.count(nums[i])) {
                return true;
            }

            // Add current element
            window.insert(nums[i]);

            // Keep window size <= k
            if (window.size() > k) {
                window.erase(nums[i - k]);
            }
        }

        return false;
    }
};