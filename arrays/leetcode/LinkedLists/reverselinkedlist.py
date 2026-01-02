# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #recursive: T O(n), M O(n)

        if not head: # if head is None return None
            return None 

        newHead = head # initialize newHead to current head
        if head.next: # if there is next node
            newHead = self.reverseList(head.next) # recursively call reverseList on next node and set newHead to result
            head.next.next = head # set next node's next pointer to current head (reversing the link)
        head.next = None # set current head's next pointer to None (to avoid cycle)

        return newHead # return newHead which is head of the reversed list