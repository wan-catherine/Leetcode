from .Utility import ListNode

class Solution(object):
    # modify the input list by reversing the lists
    def addTwoNumbers_reverse(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1

        l1 = self.reverse_list(l1)
        l2 = self.reverse_list(l2)

        c = 0
        res = ListNode()
        while True:
            value = c
            value += l1.val if l1 else 0
            value += l2.val if l2 else 0
            if value == 0 and not l1 and not l2:
                break
            c, new_value = divmod(value, 10)
            next = res.next
            res.next = ListNode(new_value)
            res.next.next = next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return res.next

    def reverse_list(self, l):
        prev = None
        cur = l
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev

    def addTwoNumbers(self, l1, l2):
        num = self.get_int(l1) + self.get_int(l2)
        res = ListNode()
        if num == 0:
            return res
        while num:
            val = num % 10
            node = ListNode(val)
            next = res.next
            res.next = node
            node.next = next
            num //= 10
        return res.next

    def get_int(self, l):
        res = 0
        while l:
            res = res*10 + l.val
            l = l.next
        return res