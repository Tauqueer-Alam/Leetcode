class Solution(object):
    def mirrorDistance(self, n):
        s=str(n)
        r=s[::-1]
        num=int(r)
        result=abs(n-num)
        return result
        