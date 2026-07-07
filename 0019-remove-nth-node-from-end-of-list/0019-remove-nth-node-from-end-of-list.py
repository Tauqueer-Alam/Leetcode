# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        count=0
        current=head
        while current:
            count+=1
            current=current.next
        if n == count:
            return head.next    
        n_last=count-n-1 
        current=head
        for i in range(n_last):
            current=current.next
        current.next=current.next.next
        return head        


