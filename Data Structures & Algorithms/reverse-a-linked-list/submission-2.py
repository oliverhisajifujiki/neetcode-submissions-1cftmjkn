# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        #classic question if linked list is: a -> b -> c -> None (all linked lists end 
        #by pointing to none)
        #the goal is: c -> b -> a -> None 
        #lots of the times for linked list we only have access to the head
        #i.e we only get a pointer to a
        #so we go along and we want to flip this pointer.
        #we first set b -> a which is simply going to do
        #a.next give b, so a.next.next = a now b is pointing to a
        #the problem is we now don't have a pointer to b.next (c) so going along is not smooth
        #therefore we must first store c 
        #b = a.next
        #tmp = b.next
        #b.next = a
        #but we want to put this in a iteratable way 
        #so cur = head
        #prev = None
        #while cur: #this works until the cur is None (end of list)
            #tmp = cur.next (holds b)
            #cur.next = prev #points a to None
            #prev = cur #now a
            #cur = tmp
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        cur = head
        prev = None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return prev #at the last step of the loop we set cur to tmp this will be none 
                    #therefore prev is last proper node value 
