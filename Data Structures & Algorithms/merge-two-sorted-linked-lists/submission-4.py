# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #temp node that always points at the head
        merged = ListNode()
        tail = merged

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            
            tail = tail.next
        
        #if we are here one or both lists are empty
        if list1 == None and list2 != None:
            tail.next = list2

        if list1 != None and list2 == None:
            tail.next = list1
        
        return merged.next





