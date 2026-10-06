from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        ans = []
        q = deque()

        for i in range(len(nums)):

            # Remove elements outside the window
            while q and q[0] <= i - k:
                q.popleft()

            # Remove smaller elements
            while q and nums[q[-1]] <= nums[i]:
                q.pop()

            q.append(i)

            # Window is ready
            if i >= k - 1:
                ans.append(nums[q[0]])

        return ans