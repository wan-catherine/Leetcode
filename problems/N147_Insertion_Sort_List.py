from .Utility import ListNode

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy = ListNode()
        dummy.next = head
        prev = head
        current = head.next
        while current:
            prev_first = dummy
            first = dummy.next
            while first.val < current.val:
                prev_first = first
                first = first.next
            if first == current:
                current = current.next
                continue
            while prev.next != current:
                prev = prev.next

            prev.next = current.next
            current.next = first
            prev_first.next = current
            current = prev.next

        return dummy.next
