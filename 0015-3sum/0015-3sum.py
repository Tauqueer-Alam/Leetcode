class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        set1=set()
        for i in range(len(nums)-2):
            left=i+1
            right=len(nums)-1
            while left<right:
                total=nums[i]+nums[left]+nums[right]
                if total==0:
                    triplet=tuple([nums[i],nums[left],nums[right]])
                    set1.add(triplet)
                    left += 1
                    right -= 1
                elif total<0:
                    left+=1
                elif total>0:
                    right-=1    

        return list(set1)       
                        
        