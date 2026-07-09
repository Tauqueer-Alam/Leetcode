class Solution(object):
    def moveZeroes(self, nums):
        l1=[]
        l2=[]
        for i in range(len(nums)):
            if nums[i]==0:
                l1.append(nums[i])
            elif nums[i]!=0:
                l2.append(nums[i]) 
        nums[:]=l2 + l1        
        return nums      
