class Solution(object):
    def findTheDifference(self, s, t):
        s_list = list(s)
        t_list = list(t)

        for i in range(len(t)):
            if t_list[i] in s_list:
                s_list.remove(t_list[i]) 
            else:
                return t_list[i]