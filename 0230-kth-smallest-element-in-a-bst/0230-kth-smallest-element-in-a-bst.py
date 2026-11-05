# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        list=[]
        def preorder(root):
            if not root:
                return None

            list.append(root.val) 
            preorder(root.left)
            preorder(root.right)   

        preorder(root)   

        list.sort()
        return list[k-1] 

