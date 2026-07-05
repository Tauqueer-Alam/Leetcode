class Solution(object):
    def twoSum(self, nums, target):
        arr = [(nums[i], i) for i in range(len(nums))]
        arr.sort()

        left = 0
        right = len(arr) - 1

        while left < right:
            s = arr[left][0] + arr[right][0]

            if s == target:
                return [arr[left][1], arr[right][1]]
            elif s > target:
                right -= 1
            else:
                left += 1

        return []