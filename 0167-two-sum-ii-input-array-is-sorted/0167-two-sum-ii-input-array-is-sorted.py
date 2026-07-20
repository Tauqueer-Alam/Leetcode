class Solution(object):
    def twoSum(self, nums, target):
        left=0
        right=len(nums)-1
        while left<right:
            s=nums[left]+nums[right]
            if s==target:
                return [left+1,right+1]
            elif s<target: 
                left+=1
            elif s>target:
                right-=1  