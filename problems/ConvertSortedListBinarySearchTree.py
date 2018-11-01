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
    def sortedListToBST(self, head):
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
        return self.helper(vals)

    def helper(self, vals):
        if vals == None or len(vals) < 1:
            return None
        middle = (len(vals) - 1) // 2
        root = TreeNode(vals[middle])
        root.left = self.helper(vals[0:middle])
        root.right = self.helper(vals[middle+1:])
        return root
