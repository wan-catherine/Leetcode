from .Utility import ListNode

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = slow = head
        has_cycle = False
        while fast and fast.next:
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
