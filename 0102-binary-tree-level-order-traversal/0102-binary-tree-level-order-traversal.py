
from collections import deque

class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []

        queue = deque([root])
        ans = []

        while queue:
            level_size = len(queue)
            level = []

            for i in range(level_size):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            ans.append(level)

        return ans
