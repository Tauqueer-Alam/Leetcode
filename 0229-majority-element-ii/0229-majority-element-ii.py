class Solution(object):
    def majorityElement(self, nums):
        req_size=len(nums)/3
        freq={}
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1

        result=[]
        for i in freq:
            if freq[i]>req_size:
                result.append(i)
        return result                    

        