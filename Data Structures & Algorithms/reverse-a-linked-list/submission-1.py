# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #so we want to flip the pointer. so for example 1 -> 2 -> 3 -> None
        #but if we flip just the first one avail we get 1 <- 2    3 -> None
        #there is no way for us to get the val 3! so we need holders 
        #we will keep track of 3 pointers cur prv and nxt 
        #save nxt = cur.next 
        #point cur.next = prv
        #move prv = cur
        #move cur = nxt
        #initialize prev with None

        prv = None
        cur = head

        while cur: #once we hit the tail the next one is None so while None stops
            #use nxt for holder
            nxt = cur.next
            #now can point to prv element we have saved
            cur.next = prv
            #update prv
            prv = cur
            #update cur with the nxt holder
            cur = nxt

        return prv
