# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        less_value=[]
        greater_value=[]
        current=head
        while current:
            if current.val<x:
                less_value.append(current.val)
                current=current.next
            elif current.val>=x:
                greater_value.append(current.val)
                current=current.next

        new_list= less_value + greater_value

        dummy=ListNode(0)
        current=dummy
        for i in new_list:
            current.next=ListNode(i)
            current=current.next

        return dummy.next    



