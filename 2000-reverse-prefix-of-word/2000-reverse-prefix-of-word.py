class Solution(object):
    def reversePrefix(self, word, ch):
        for i in range(len(word)):
            if word[i]==ch:
                left_str=word[:i+1]
                right_str=word[i+1:]
                rev_left_str=left_str[::-1]
                result=rev_left_str + right_str
                return result 

        return word                                                                           
        