# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def length(self, head):
        current=head
        count=0
        while current!=None:
            count=count+1
            current=current.next
        return count    


    def middleNode(self, head):
        count=self.length(head)
        mid=count//2
        current=head
        for i in range(mid):
            current=current.next
        return current

        