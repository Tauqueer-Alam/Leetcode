class Solution:
    def twoSum(self, nums, target):
        arr = {}

        n=len(nums)

        for i in range(n):

            first=nums[i]
            second=target-first

            if second in arr:
                return [i,arr[second]]

            arr[first]=i    