class Solution(object):
    def minPartitions(self, n):
        largest = 0

        for digit in n:
            largest = max(largest, int(digit))

        return largest