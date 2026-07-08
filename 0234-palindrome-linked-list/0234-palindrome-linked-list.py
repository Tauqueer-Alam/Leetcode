# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        current=head
        li=[]
        while current:
            li.append(current.val)
            current=current.next
        if li==li[::-1]:
            return True
        else:
            return False        

