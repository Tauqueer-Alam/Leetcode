class Solution(object):
    def majorityElement(self, nums):
        freq={}

        for x in nums:
            if x in freq:
                freq[x]+=1

            else:
                freq[x]=1

        return max(freq, key=freq.get)       

