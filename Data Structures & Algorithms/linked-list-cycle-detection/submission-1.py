# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tort = head
        hare = head
        while hare and hare.next:
            hare = hare.next.next
            tort = tort.next

            if hare == tort:
                return True
        return False
