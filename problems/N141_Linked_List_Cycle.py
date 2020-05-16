from .Utility import ListNode
"""
use fast and slow point
if there is a cycle in the list , fast will meet slow finally
"""
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        fast = slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False