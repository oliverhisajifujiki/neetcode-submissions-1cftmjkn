# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #if its empty just return None
        if not lists:
            return None

        while len(lists) > 1:
            mergedLists = []

            #step through the lists 2 at a time
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                if i + 1 < len(lists): #there is indeed another list
                    l2 = lists[i+1]
                else:
                    l2 = None
                
                #merge the two sorted linked lists
                merged = self.mergeTwoLists(l1,l2)

                #store
                mergedLists.append(merged)

            #after one whole round relpace lists
            lists = mergedLists

        return lists[0] #this will have the big merged list lists is still a list and we want to return a listnode 

    def mergeTwoLists(self, list1, list2):

        dummy = ListNode()

        tail = dummy #always points to the last node in the merged list so far

        while list1 and list2: #while both lists still have nodes left
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next #move list1 forward
            else:
                tail.next = list2
                list2 = list2.next #move list2 forward

            #update tail
            tail = tail.next

        #attach the remainder (if remainder exists)
        if list1: #list1 is not None
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next
        