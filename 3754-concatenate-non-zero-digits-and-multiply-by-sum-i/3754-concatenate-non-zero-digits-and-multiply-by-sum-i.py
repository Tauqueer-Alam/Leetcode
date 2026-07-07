class Solution(object):
    def sumAndMultiply(self, n):
        string = str(n)
        li = list(string)
        new_li = list(map(int, li))

        final_list = []

        for i in range(len(new_li)):
            if new_li[i] != 0:
                final_list.append(new_li[i])

        if len(final_list) == 0:
            return 0

        sum1 = sum(final_list)
        x = int(''.join(map(str, final_list)))

        return x * sum1