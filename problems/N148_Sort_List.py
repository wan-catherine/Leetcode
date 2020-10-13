""""
This is merge sort problem. If it's in array, it will be much easier, but here it's a link-list.
I spent two hours to fix it !!!

The key point here is , you need to dump Listnode : head = temp = ListNode()
Then each time , when you merge the listnode , use temp.next = *, then temp = temp.next .
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def sortList_before(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return

        end, length = self.get_length(head)
        return self.merge(head, end, length)

    def get_length(self, head):
        length = 1
        temp = head
        while temp.next:
            temp = temp.next
            length += 1
        return temp, length

    def merge_(self, head, end, length):
        if head == end:
            return head

        mid = length // 2
        left, right = head, head

        i = 0
        while i < mid:
            left_end = right
            right = right.next
            i += 1

        left_end.next = None
        left = self.merge(left, left_end, mid)
        right = self.merge(right, end, length - mid)

        head = temp = ListNode()
        while left and right:
            if left.val < right.val:
                temp.next= left
                left = left.next
            else:
                temp.next = right
                right = right.next

            if head:
                head = temp
            temp = temp.next
        if left:
            temp.next = left
        if right:
            temp.next = right
        return head.next

    def sortList_recursion(self, head):
        if not head or not head.next:
            return head

        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        def merge(l1, l2):
            head = temp = ListNode()
            while l1 and l2:
                if l1.val > l2.val:
                    temp.next = l2
                    l2 = l2.next
                else:
                    temp.next = l1
                    l1 = l1.next
                if not head:
                    head = temp
                temp = temp.next
            if l1:
                temp.next = l1
            if l2:
                temp.next = l2
            return head.next

        mid = slow.next
        slow.next = None
        return merge(self.sortList(head), self.sortList(mid))

    def sortList(self, head):
        def merge(l1, l2, head):
            cur = head
            while l1 and l2:
                if l1.val > l2.val:
                    cur.next = l2
                    l2 = l2.next
                else:
                    cur.next = l1
                    l1 = l1.next
                cur = cur.next
            cur.next = l1 if l1 else l2
            while cur.next:
                cur = cur.next
            return cur

        def split(head, n):
            while n-1 and head:
                head = head.next
                n -= 1

            if not head:
                return None

            new_head = head.next
            head.next = None
            return new_head

        if not head or not head.next:
            return head

        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next

        dummy = ListNode(0)
        dummy.next = head
        step = 1
        while step < length:
            cur = dummy.next
            tail = dummy
            while cur:
                left = cur
                right = split(left, step)
                cur = split(right, step)
                tail = merge(left, right, tail)
            step = step << 1
        return dummy.next
