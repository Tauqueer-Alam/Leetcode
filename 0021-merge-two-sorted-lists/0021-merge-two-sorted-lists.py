# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy=ListNode(0)
        current=dummy
        temp_list=[]

        while list1:
            temp_list.append(list1.val)
            list1=list1.next

        while list2:
            temp_list.append(list2.val)
            list2=list2.next 

        temp_list.sort()



        for i in temp_list:
            current.next = ListNode(i)
            current = current.next

        return dummy.next           



        
        