class Solution(object):
    def reverseVowels(self, s):
        li = list(s)
        new_list = []
        index = []

        for i in range(len(li)):
            if li[i] in "aeiouAEIOU":
                new_list.append(li[i])
                index.append(i)

        new_list.reverse()

        j = 0
        for i in index:
            li[i] = new_list[j]
            j += 1

        return "".join(li)