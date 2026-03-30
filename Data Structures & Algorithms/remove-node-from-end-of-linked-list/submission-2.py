# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #idea is to have to pointers that are n apart and then if you progress the forward one
        #until it reaches the tail (None)
        #the slower one will be n from the end

        #need dummy nodes incase we are removing the head

        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy
        i = 0

        while i < n + 1:
            fast = fast.next #now fast is n steps ahead
            i = i + 1

        while fast: #once we reach the tail slow will now be n away from tail
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return dummy.next

