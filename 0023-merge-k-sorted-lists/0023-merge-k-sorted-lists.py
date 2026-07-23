# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        new_list=[]
        for head in lists:
            while head:

                new_list.append(head.val)
                head=head.next


        new_list.sort()

        dummy=ListNode(0)
        current=dummy
        for i in range(len(new_list)):
            current.next=(ListNode(new_list[i]))
            current=current.next

        return dummy.next    



