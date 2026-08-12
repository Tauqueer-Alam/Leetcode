# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):

        if not head or not head.next:
            return head

        # Find length
        n = 0
        current = head

        while current:
            n += 1
            current = current.next

        k = k % n

        if k == 0:
            return head

        # Find new tail
        current = head

        for i in range(n - k - 1):
            current = current.next

        # New head
        new_head = current.next

        # Break
        current.next = None

        # Find last node
        tail = new_head

        while tail.next:
            tail = tail.next

        # Connect
        tail.next = head

        return new_head