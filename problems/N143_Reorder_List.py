from .Utility import ListNode
"""
1. find the middle node : two pointers(slow and fast pointers)
2. split into seperate list
3. reverse the second list
4. merge two lists
"""
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        slow,fast = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        l1 = head  # first half of the list
        l2 = slow.next  # second half of the list
        slow.next = None

        # reverse the second half of the list
        prev = None
        current = l2
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        l2 = prev

        while l1 or l2:
            n_l1 = l1.next
            if l2:
                n_l2 = l2.next
                l2.next = n_l1
            l1.next = l2
            l1 = n_l1
            l2 = n_l2

        # while l1 and l2:
        #     new_l1 = l1.next
        #     new_l2 = l2.next
        #     l2.next = new_l1
        #     l1.next = l2
        #     l1 = new_l1
        #     l2 = new_l2
