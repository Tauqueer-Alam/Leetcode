class Solution(object):
    def maxProduct(self, nums):
        n = len(nums)
        result = []

        for i in range(n):
            for j in range(i + 1, n):
                result.append((nums[i] - 1) * (nums[j] - 1))

        return max(result)