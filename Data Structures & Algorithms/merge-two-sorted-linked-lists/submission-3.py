# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = ListNode() #init and a holder for the head
        tail = merged #this is the variable we will use to add onto the merged

        while list1 and list2: #go until one is empty 
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        #one or both of the lists are empty 
        if list1 == None and list2 != None:
            tail.next = list2
        
        elif list1 != None and list2 == None:
            tail.next = list1
        
        #both lists are empty we are indeed done

        merged = merged.next

        return merged 

