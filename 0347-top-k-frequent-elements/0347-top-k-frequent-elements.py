import heapq

class Solution(object):
    def topKFrequent(self, nums, k):

        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        heap = []

        for num, count in freq.items():

            heapq.heappush(heap, (count, num))

            if len(heap) > k:
                heapq.heappop(heap)
        ans = []

        while heap:
            ans.append(heapq.heappop(heap)[1])

        return ans