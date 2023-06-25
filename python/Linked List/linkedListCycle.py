# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Tortiose and Hare
        # O(n) O(1)
        # fast and slow will always meet because the distance between them will always decrease by 1
        slow, fast = head, head
        # fast.next becuase it increases by 2
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False
