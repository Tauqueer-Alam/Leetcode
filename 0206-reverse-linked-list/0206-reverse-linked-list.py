# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        current=head
        prev=None

        while current!=None:

            next_node = current.next   # Store next node
            current.next = prev        # Reverse the link
            prev = current             # Move prev forward
            current = next_node        # Move current forward

        return prev
        