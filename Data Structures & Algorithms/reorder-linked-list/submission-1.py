# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #the reordering is strict
        #if each element is e_i e.g. [e_0 -> e_1 -> e2 -> e3 -> e4 -> none]
        # the reordering is [e_0 -> e_4 -> e_1 -> e_3 -> e_2 -> None]
        # first -> last -> second -> second last -> third -> third last -> ...
        # the general idea is split in half
        # reverse second half
        # alternate merge 

        #split logic
        slow = head
        fast = head.next #i think the only way to do this without memorizing is doing an example of size 4 and 5 

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #so when the fast goes twice as fast, so when it ends slow should be in the middle

        second = slow.next #start the next list 
        slow.next = None #end the first list before the next one starts

        #reverse logic
        #to reverse we need a nxt (tmp var), cur, prv . 1 -> 2 -> 3 -> None
        #initialize prv = None cur = head (1)
        # while cur: 
        # nxt = cur.next (2)
        #cur.next = prv     None <- 1
        #prv = cur (1) 
        #cur = nxt (2)
        #then we loop

        prv = None
        cur = second

        while cur:
            nxt = cur.next
            cur.next = prv
            prv = cur
            cur = nxt

        second = prv #prv holds the last current which now becomes the head

        #merge first = head and second
        first = head

        #this is not the same thing as the sorted merge
        #we simply have to hold both nexts in temp variables 
        #and then upda
        while second: #with how we split second is always <= to first so we can just check this
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            first.next.next = tmp1
            first = tmp1
            second = tmp2
        

        


