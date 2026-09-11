class Solution(object):
    def containsDuplicate(self, nums):
        unique=set()
        n=len(nums)

        for i in range(n):
            if nums[i] in unique:
                return True
            else:
                unique.add(nums[i])   

        return False         
        