class Solution(object):
    def intersection(self, nums1, nums2):
        intersect=set(nums1).intersection(set(nums2))
        return list(intersect)
        