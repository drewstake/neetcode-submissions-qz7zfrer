# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #if curr1 >= curr2:
        #   add curr 2
        #else:
        #   add curr1
        dummy = ListNode(0)
        tail = dummy
        curr1 = list1
        curr2 = list2

        while curr1 or curr2:
            if curr1 and curr2:
                if curr1.val <= curr2.val:
                    tail.next = curr1
                    curr1 = curr1.next
                else:
                    tail.next = curr2
                    curr2 = curr2.next
            elif curr1 and not curr2:
                tail.next = curr1
                curr1 = curr1.next
            else:
                tail.next = curr2
                curr2 = curr2.next
            tail = tail.next
        return dummy.next
                
