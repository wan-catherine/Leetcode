from .Utility import ListNode, TreeNode

class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        prefix_mapping = {}
        sum = 0
        while cur:
            sum += cur.val
            prefix_mapping[sum] = cur
            cur = cur.next

        cur = dummy
        sum = 0
        while cur:
            sum += cur.val
            cur.next = prefix_mapping[sum].next
            cur = cur.next
        return dummy.next




