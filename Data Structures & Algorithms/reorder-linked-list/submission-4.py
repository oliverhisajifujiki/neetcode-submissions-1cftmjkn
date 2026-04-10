# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #the first thing we need to do is figure out how to split this linked list in half
        #we will use an idea of a fast marker and a slow marker

        fast = head.next
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        second = slow.next
        slow.next = None
        first = head

        #split done, note that first is always either equal to second (in size)
            #or one element bigger
        
        #now we want to reverse the second LL
        cur = second
        prev = None

        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        second = prev

        while second:
            
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            first.next.next = tmp1


            first = tmp1
            second = tmp2
        



    def printLL(self, head):
        cur = head
        while cur:
            print(cur.val, end = "->")
            cur = cur.next
        print("None")
            