class Solution(object):
    def moveZeroes(self, nums):
        temp=[]
        n=len(nums)

        for i in range(n):
            if nums[i]!=0:
                temp.append(nums[i])

        for i in range(len(temp)):
            nums[i]=temp[i]

        for i in range(len(temp),n):
            nums[i]=0    

        return nums             

        