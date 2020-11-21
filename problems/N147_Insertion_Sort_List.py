from .Utility import ListNode

class Solution(object):
    def insertionSortList_(self, head):
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

    """
    20201120 update
    """
    def insertionSortList(self, head):
        dummy = ListNode(0)
        while head:
            start = dummy
            while start.next and start.next.val < head.val:
                start = start.next
            next_node = start.next
            start.next = head
            head = head.next
            start.next.next = next_node
        return dummy.next
