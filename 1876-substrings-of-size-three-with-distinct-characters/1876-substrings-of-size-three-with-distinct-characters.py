class Solution(object):
    def countGoodSubstrings(self, s):
        k=3
        arr=list(s)
        window = arr[:k]
        count=0
        if len(set(window)) == k:
            count += 1


        for i in range(1, len(arr) - k + 1):
            window.pop(0)
            window.append(arr[i + k - 1])
            window_set=set(window)

            if len(window_set)==k:
                count+=1

        return count        


        