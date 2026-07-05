class Solution(object):
    def longestOnes(self, nums, k):
        left = 0
        zero_count = 0
        ans = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count += 1

            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            ans = max(ans, i - left + 1)

        return ans