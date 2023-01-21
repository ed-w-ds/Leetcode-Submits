# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Iterative:
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Time: O(n) | Space: O(1)
        prev = None
        current = head
        while current:
          nxt = current.next # use to not break the link and lose the linked list
          current.next = prev
          prev = current
          current = nxt
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
