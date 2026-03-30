# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #classic tort and hare solution exists
        #once we enter a cycle we can never leave it 
        #so we set the tort to be a slow traverser 
        #and hare to be a faster one 
        #eventually they must meet 
        tort = head
        hare = head
        while hare and hare.next: #note we do not need to check tort as if we run into problems hare will reach it faster
            hare = hare.next.next
            tort = tort.next
        
            if tort == hare:
                return True
            
        return False
        