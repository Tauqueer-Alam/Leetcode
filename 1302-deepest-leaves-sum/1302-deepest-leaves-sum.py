# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        self.ans = 0
        self.max_depth = -1

        def dfs(node, depth):
            if not node:
                return

            if not node.left and not node.right:
                if depth > self.max_depth:
                    self.max_depth = depth
                    self.ans = node.val
                elif depth == self.max_depth:
                    self.ans += node.val

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return self.ans