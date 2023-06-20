
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Iterative - Time: O(n) | Space: O(1)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None
    
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev

      
# Recursive Time: O(n) | Space: O(n)
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        reverseHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return reverseHead
