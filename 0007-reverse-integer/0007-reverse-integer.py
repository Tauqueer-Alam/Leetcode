class Solution(object):
    def reverse(self, x):
        if x<0:
            value_neg=True
            x=-x
        else:
            value_neg=False    
        string=str(x)
        rev=string[::-1]
        integer=int(rev)
        if value_neg==True:
            ans=-integer
        else:
            ans=integer    
        

        if -2**31 <= ans <= 2**31 - 1:
            return ans
        else:
            return 0
            