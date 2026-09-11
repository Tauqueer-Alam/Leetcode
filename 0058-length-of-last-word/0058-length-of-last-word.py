class Solution(object):
    def lengthOfLastWord(self, s):
        li=s.split()
        return len(li[-1])
        