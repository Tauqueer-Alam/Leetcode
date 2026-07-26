"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        ans=[]

        def dfs(node):
            if not node:
                return 

            ans.append(node.val)

            for i in node.children:
                dfs(i)
        
        dfs(root)
        return ans        


        