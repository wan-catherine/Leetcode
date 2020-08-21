# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST_before(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head == None:
            return None
        vals = []
        while head != None:
            vals.append(head.val)
            head = head.next
        return self.helper_before(vals)

    def helper_before(self, vals):
        if vals == None or len(vals) < 1:
            return None
        middle = (len(vals) - 1) // 2
        root = TreeNode(vals[middle])
        root.left = self.helper(vals[0:middle])
        root.right = self.helper(vals[middle+1:])
        return root

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        return self.helper(head)

    def helper(self, head):
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        root = TreeNode(slow.val)
        #need to check if left is already empty.
        if slow != head:
            left = head
            while left != slow and left.next != slow:
                left = left.next

            left.next = None
            root.left = self.helper(head)
        else:
            root.left = None
        right = slow.next
        slow.next = None

        root.right = self.helper(right)
        return root
