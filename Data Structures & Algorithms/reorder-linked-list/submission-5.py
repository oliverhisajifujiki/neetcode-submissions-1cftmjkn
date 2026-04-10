# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #the first step is to split the linked list 
        fast = head.next
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        second = slow.next
        slow.next = None
        first = head

        #splitting done, now we need to reverse second
        cur = second
        prev = None

        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        second = prev

        #done now we must merge

        #second is always smaller 

        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            first.next.next = tmp1
            first = tmp1
            second = tmp2

        print("should be merged", end=":")
        self.printLL(head)
        



    def printLL(self, head):
        cur = head
        while cur:
            print(cur.val, end="->")
            cur = cur.next
        
        print("None")



