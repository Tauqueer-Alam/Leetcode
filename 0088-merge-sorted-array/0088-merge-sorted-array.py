class Solution(object):
    def merge(self, nums1, m, nums2, n):
        new_arr = []

        for i in range(m):
            new_arr.append(nums1[i])

        for i in range(n):
            new_arr.append(nums2[i])

        new_arr.sort()

        for i in range(m + n):
            nums1[i] = new_arr[i]