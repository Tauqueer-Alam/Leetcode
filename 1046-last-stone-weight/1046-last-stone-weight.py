import heapq
class Solution(object):
    def lastStoneWeight(self, stones):
        heap=[]

        for i in stones:
            heapq.heappush(heap,-i)

        while len(heap)>1:
            a=-heapq.heappop(heap)
            b=-heapq.heappop(heap)

            if a!=b:
                heapq.heappush(heap,-(a-b))

        if len(heap)==1:
            return -heap[0]

        else:
            return 0            
        
        