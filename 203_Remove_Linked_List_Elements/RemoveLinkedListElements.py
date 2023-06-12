# Understand
# Input: head of linked list, integer val
# Output: new head without any nodes with val

''' Example
1) Empty head --> none

2) Begin: head: 1   val: 1 => none

3) Middle: head: 1->2->3->1 val: 2 ==> 1->3->1

4) head; 1->2->3->4 val: 4 ==> 1->2->3
'''

# Match:
# 1. basic linked list operation
# 2. dummy node

'''
# Plan:
# 1) create a dummy node, its next is head
# 2) set up ptr prev = dummy and curr = head
# 3) while curr is not none:
#    if curr.val is equal to val:
#       prev.next = curr.next
#    else: prev = curr
#    curr = curr.next
# 4. return dummy.next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        curr = head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return dummy.next
    
'''

'''
# One pointer solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        curr = head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return dummy.next
'''

'''
Without using dummy node
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:


        # while the head == val:
        #. move head to head.next
        while head and head.val == val:
            head = head.next
            
        # 1. empty
        if head is None:
            return None

        curr = head.next
        prev = head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return head
'''

'''
# Recursive solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Base case:
        if head is None:
            return None
        
        # General case:
        head.next = self.removeElements(head.next,val)
        if head.val == val:
            head = head.next
        return head

'''