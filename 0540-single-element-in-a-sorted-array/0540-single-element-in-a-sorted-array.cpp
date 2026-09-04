class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        int n = nums.size();

        if (n == 1)
            return nums[0];

        int left = 0;
        int right = n - 1;

        while (left <= right) {
            int mid = (left + right) / 2;

            // Check first element
            if (mid == 0 && nums[0] != nums[1])
                return nums[mid];

            // Check last element
            else if (mid == n - 1 && nums[n - 1] != nums[n - 2])
                return nums[mid];

            // Check if mid itself is single
            else if (nums[mid] != nums[mid + 1] &&
                     nums[mid] != nums[mid - 1])
                return nums[mid];

            // mid is even
            else if (mid % 2 == 0) {

                if (nums[mid - 1] == nums[mid]) {
                    right = mid - 1;
                }
                else {
                    left = mid + 1;
                }
            }

            // mid is odd
            else {

                if (nums[mid - 1] == nums[mid]) {
                    left = mid + 1;
                }
                else {
                    right = mid - 1;
                }
            }
        }

        return -1;
    }
};