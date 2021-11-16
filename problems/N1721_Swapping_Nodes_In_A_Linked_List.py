from Utility import ListNode
"""
when we get lslow, lfast, rslow, rfast, we need to consider two corner case:
    lfast.next == rfast
    rfast.next == lfast
"""
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        total = 0
        cur = dummy
        while cur.next:
            cur = cur.next
            total += 1
        lfast, lslow = head, dummy
        c = k - 1
        while c:
            lfast = lfast.next
            lslow = lslow.next
            c -= 1
        rfast, rslow = head, dummy
        c = total - k
        while c:
            rfast = rfast.next
            rslow = rslow.next
            c -= 1
        if lfast.next == rfast:
            rnext = rfast.next
            lslow.next = rfast
            rfast.next = lfast
            lfast.next = rnext
        elif rfast.next == lfast:
            lnext = lfast.next
            rslow.next = lfast
            lfast.next = rfast
            rfast.next = lnext
        else:
            lnext = lfast.next
            rnext = rfast.next
            lslow.next = rfast
            rfast.next = lnext
            rslow.next = lfast
            lfast.next = rnext
        return dummy.next