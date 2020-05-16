from .Utility import ListNode

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return
        odd_node = head
        even_head = even_node = head.next

        while odd_node and even_node:
            if even_node.next:
                odd_node.next = even_node.next
                odd_node = odd_node.next
            else:
                break
            even_node.next =odd_node.next
            even_node = even_node.next

        odd_node.next = even_head
        return head