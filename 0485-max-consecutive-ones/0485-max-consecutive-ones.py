class Solution(object):
    def findMaxConsecutiveOnes(self, nums):

        maximum=0
        consecutive=0
        for i in range(len(nums)):
            if nums[i]==1:
                consecutive+=1
                maximum=max(maximum,consecutive)
            else:
                consecutive=0   

        return maximum        



        