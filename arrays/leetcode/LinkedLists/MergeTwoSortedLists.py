#You are given the heads of two sorted linked lists list1 and list2.

#Merge the two lists into one sorted linked list and return the head of the new sorted linked list.

#The new list should be made up of nodes from list1 and list2.




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() #dummy node is used to simplify edge cases (like when one of the lists is empty)
        tail = dummy #tail is used to keep track of the current node in the new list
        while list1 and list2: #while both lists are not empty (looping through all the nodes)
            if list1.val < list2.val: #ensure that list comes in a sorted way, not list1 + list2 but list1 and list2 merged clean
                tail.next = list1 #adds the current node in list1 to the new list
                list1 = list1.next #continue to the next node in line (of list1)
            else: #if list2 is smaller
                tail.next = list2 #add current node in list2 to the new list
                list2 = list2.next #continue to the next node in line (of list2)
            tail = tail.next #continue to the next node in line (of the new list)
        
        if list1: #if list1 is not empty, add the rest of list1 to the new list
            tail.next = list1 #add the rest of list1 to the new list
        elif list2: #if list2 is not empty, add the rest of list2 to the new list
            tail.next = list2 #add the rest of list2 to the new list
        
        return dummy.next
    