class Solution(object):
    def findDuplicates(self, nums):
        freq={}
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1    

        ans=[]

        for i in freq:
            if freq[i]==2:
                ans.append(i)        

        return ans        

