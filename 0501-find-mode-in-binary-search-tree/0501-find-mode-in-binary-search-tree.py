# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        lst = []

        def inorder(root):
            if not root:
                return

            inorder(root.left)
            lst.append(root.val)
            inorder(root.right)

        inorder(root)

        freq={}
        for i in lst:
            if i in freq:
                freq[i]+=1

            else:
                freq[i]=1

        max_val=max(freq.values()) 

        ans=[]

        for i in freq:
            if freq[i]==max_val:
                ans.append(i)

        return ans                