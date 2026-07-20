# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        li=[]
        current=head
        while current:
            li.append(current.val)
            current=current.next

        li[k-1],li[len(li)-k]=li[len(li)-k],li[k-1]

        dummy=ListNode(0)
        current=dummy
        for i in li:
            current.next=ListNode(i)
            current=current.next

        return dummy.next        

        