class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        set1=set()
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                left=j+1
                right=len(nums)-1
                while left<right:
                    total=nums[i]+nums[j]+nums[left]+nums[right]
                    if total==target:
                        triplet=tuple(sorted([nums[i],nums[j],nums[left],nums[right]]))
                        set1.add(triplet)
                        left += 1
                        right -= 1
                    elif total<target:
                        left+=1
                    elif total>target:
                        right-=1    
        return list(set1)
        