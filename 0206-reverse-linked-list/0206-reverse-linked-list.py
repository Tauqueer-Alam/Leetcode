# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        li=[]

        current=head

        while current:
            li.append(current.val)
            current=current.next

        li.reverse()    
        
        if len(li)==0:
            return None

        newhead=ListNode(li[0])
        current=newhead
        for i in range(1,len(li)):
            current.next=ListNode(li[i])   
            current=current.next

        return newhead     
        