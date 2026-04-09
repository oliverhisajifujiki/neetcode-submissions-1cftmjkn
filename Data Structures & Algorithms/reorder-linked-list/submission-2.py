# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #first step is to split the list into two lists
        fast = head.next
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        second = slow.next #we start the second list the element after our "middle"
        #useful to know that if LL is even, second and first lists will be the same
        #if LL is odd second will have one less element than first
        first = head
        slow.next = None #this alters the LL so that after our middle it stops! 
        
        # print("second")
        # self.printLL(second)
        # print("first")
        # self.printLL(first)

        #splitting done
        #now onto reversing the second linked list

        cur = second
        prev = None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        second = prev 

        #reversing second list done

        #we now merge the lists

        

        while second: #because this is the smaller list we just go until its empty
                        #and we make sure hte tail is pointing the whatever is .next for the first
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            first.next.next = tmp1
            first = tmp1
            second = tmp2
            


    
    def printLL(self, head: Optional[ListNode]):
        current = head 
        while current:
            print(current.val, end="->")
            current = current.next
        print("None")
            