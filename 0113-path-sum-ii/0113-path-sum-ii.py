# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def pathSum(self, root, targetSum):
        ans = []

        def dfs(node, path):
            if not node:
                return

            path.append(node.val)

            if not node.left and not node.right:
                ans.append(path[:])   
            else:
                dfs(node.left, path)
                dfs(node.right, path)

            path.pop()  

        dfs(root, [])

        result = []
        for arr in ans:
            if sum(arr) == targetSum:
                result.append(arr)

        return result