# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #okay first we have to check if list1.val (which should be a head) < list2.val
        #wlog say we can start with list1.val and then check if list1.next < list2.val
        #now we either update the next pointer to list2 or not 
        #and we just go until one of them points to None

        merged = ListNode() #init important
        tail = merged

        while list1 and list2: 
            if list1.val < list2.val: #point to list1
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            
            tail = tail.next #update what our tail now is
        
        #we are out of the while loop so one or both list1/list2 is None
        if list1: #this means that list1 still has more 
            tail.next = list1
        
        else: #this else is safe even if both are None because we would just point to None which is wat the tail should be pointing at anyways
            tail.next = list2
        
        return merged.next

