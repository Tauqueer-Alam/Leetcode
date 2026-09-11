class Solution:
    def twoSum(self, nums, target):
        arr = {}

        for i in range(len(nums)):
            first = nums[i]
            second = target - first

            if second in arr:
                return [i, arr[second]]

            arr[first] = i

        return []