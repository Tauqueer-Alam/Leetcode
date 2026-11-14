class Solution(object):
    def maxScore(self, cardPoints, k):
        n = len(cardPoints)
        left_sum = 0
        right_sum = 0
        maxsum = 0

        for i in range(k):
            left_sum += cardPoints[i]

        maxsum = left_sum

        right_index = n - 1

        for i in range(k):
            left_sum -= cardPoints[k-1-i]
            right_sum += cardPoints[right_index]
            right_index -= 1

            maxsum = max(maxsum, left_sum + right_sum)

        return maxsum