class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        list_s1=s1.split()
        list_s2=s2.split()

        freq1={}
        freq2={}

        for word in list_s1:
            if word in freq1:
                freq1[word] += 1
            else:
                freq1[word] = 1


        for word in list_s2:
            if word in freq2:
                freq2[word] += 1
            else:
                freq2[word] = 1

        ans = []

        # Check words from s1
        for word in freq1:
            if freq1[word] == 1 and word not in freq2:
                ans.append(word)

        # Check words from s2
        for word in freq2:
            if freq2[word] == 1 and word not in freq1:
                ans.append(word)

        return ans