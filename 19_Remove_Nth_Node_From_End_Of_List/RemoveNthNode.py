# Understand 
# Input: head of the list, integer n

# Output: head of list

# Constraints: list length >= 1

# Match: recursion 

# Plan:
# base case: if head is None, return [None, 0]
# general case:
#  1. [head.next, index] = removeItem(head.next)
#  2. if index + 1 == n:
#        return [head.next, index + 1]
#     else:
#        return [head, index]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        def removeItem(head):
            # base case
            if head is None:
                return [None, 0]
            
            # general case
            head.next, i = removeItem(head.next)
            i += 1
            if i == n:
                return [head.next, i]
            else: return [head, i]

        return removeItem(head)[0]