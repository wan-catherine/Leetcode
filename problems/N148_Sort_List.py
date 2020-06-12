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
    def sortList(self, head):
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

    def merge(self, head, end, length):
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




