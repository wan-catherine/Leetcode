from .Utility import ListNode

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        fast = slow = head
        has_cycle = False
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                has_cycle = True
                break

        if not has_cycle:
            return None

        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
