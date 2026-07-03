class Solution(object):
    def reverseWords(self, s):
        list=s.split()
        n=len(list)
        new_list=[]
        for i in range(n):
            new_list.append(list[i][::-1])

        return " ".join(new_list)