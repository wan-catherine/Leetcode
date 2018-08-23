# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if lists == []:
            return None

        if len(lists) == 1:
            return lists[0]

        head = lists[0]
        i = 1
        while i < len(lists):
            head = self.merge(head, lists[i])
            i += 1
        return head

    def merge(self, first, second):
        head = ListNode(0)
        tmp = head
        while first != None and second != None:
            if first.val <= second.val:
                tmp.next = first
                first = first.next
            else:
                tmp.next = second
                second = second.next
            tmp = tmp.next
        if first != None:
            tmp.next = first
        elif second != None:
            tmp.next = second

        return head.next



