# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        current=head
        li=[]
        while current:
            li.append(current.val)
            current=current.next


        desired_list=[]
        for i in range(len(li)):
            if li.count(li[i])==1:
                desired_list.append(li[i])
        
        if not desired_list:
            return None

        newhead=ListNode(desired_list[0]) 
        current=newhead 

        for i in range(1,len(desired_list)):
            current.next=ListNode(desired_list[i])
            current=current.next

        return newhead    
            




        