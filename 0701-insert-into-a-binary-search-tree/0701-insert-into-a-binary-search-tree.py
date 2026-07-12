# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, target):
        if not root:
            return TreeNode(target)

        current=root
        while current!=None:
            if current.val==target:
                return root
            elif current.val>target:
                if current.left==None:
                    current.left=TreeNode(target)
                    break
                current=current.left    

            elif current.val<target:
                if current.right==None:
                    current.right=TreeNode(target) 
                    break
                current=current.right    

        return root                   

        
        