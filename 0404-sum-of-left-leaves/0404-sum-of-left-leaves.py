# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):

        def dfs(node):
            if not node:
                return 0

            ans = 0

            if node.left and not node.left.left and not node.left.right:
                ans += node.left.val

            ans += dfs(node.left)
            ans += dfs(node.right)

            return ans

        return dfs(root)