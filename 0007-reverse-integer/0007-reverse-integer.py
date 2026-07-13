class Solution(object):
    def reverse(self, x):
        if x<0:
            string=str(-x)
            rev=int(string[::-1])
            rev=-rev
            if rev < -(2**31) or rev > 2**31 - 1:
                return 0
            return rev

        else:
            string=str(x)
            rev=int(string[::-1])
            if rev < -(2**31) or rev > 2**31 - 1:
                return 0
            return rev
        