# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #the idea is to send a pointer n steps ahead,
        #then send another pointer and increment both pointers at the same time
        #when the faster pointer reaches the end, the slower pointer should be n steps from the end

        #we need dummy start incase we are removing the head

        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy

        for i in range(n + 1): #has to be n plus 1 cuz of dummy
            fast = fast.next 
        
        #now fast should be n ahead

        while fast:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next #skips the element we wanted to erase

        return dummy.next 



    def printLL(self, head):
        cur = head
        while cur:
            print(cur.val, end="->")
            cur = cur.next
        
        print("None")
