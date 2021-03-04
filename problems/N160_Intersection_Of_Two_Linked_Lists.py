class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        f, s = headA, headB

        while f != s:
            if not f:
                f = headB
            else:
                f = f.next

            if not s:
                s = headA
            else:
                s = s.next
        return f
