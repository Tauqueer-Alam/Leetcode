class Solution(object):
    def longestNiceSubstring(self, s):
        ans=""
        for i in range(len(s)):
            for j in range(i,len(s)):
                sub=s[i:j+1]
                char=set(sub)
                nice=True
                for ch in char:
                    if ch.lower() not in char or ch.upper() not in char:
                        nice=False
                        break
                if nice and len(sub) > len(ans):
                    ans = sub  
        return ans