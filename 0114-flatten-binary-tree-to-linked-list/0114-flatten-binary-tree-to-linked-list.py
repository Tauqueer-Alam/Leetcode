# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        if root is None:
            return

        # Flatten left and right subtrees
        self.flatten(root.left)
        self.flatten(root.right)

        # Save the flattened left and right subtrees
        left = root.left
        right = root.right

        # Move left subtree to the right
        root.left = None
        root.right = left

        # Find the tail of the new right subtree
        current = root
        while current.right:
            current = current.right

        # Attach the original right subtree
        current.right = right