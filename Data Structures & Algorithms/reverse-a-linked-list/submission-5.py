# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head # head = [1,2,3,4,5]
        
        while curr: # while not null
            nxt = curr.next # 2
            curr.next = prev # None <- 1 <- 2
            prev = curr # 1
            curr = nxt # 2
            
        return prev
            
            