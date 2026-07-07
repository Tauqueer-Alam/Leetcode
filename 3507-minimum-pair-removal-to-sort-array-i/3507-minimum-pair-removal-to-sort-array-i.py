class Solution(object):
    def minimumPairRemoval(self, nums):
        count=0
        while nums!=sorted(nums):
            min_sum = float('inf')
            index=-1
            for i in range(len(nums)-1):
                sum=nums[i]+nums[i+1]
                if sum<min_sum:     
                    min_sum=sum
                    index=i

            nums[index]=min_sum
            nums.pop(index+1)
            count+=1
        return count    
