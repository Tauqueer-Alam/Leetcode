# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def largestValues(self, root):
        if not root:
            return []
        ans=[]
        queue=deque([root])  

        while queue:
            max_val=float('-inf')
            for i in range(len(queue)):
                node=queue.popleft() 
                max_val=max(max_val,node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(max_val)

        return ans    

        