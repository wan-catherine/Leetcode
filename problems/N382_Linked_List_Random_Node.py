# Definition for singly-linked list.
import random
"""
reservior sampling algorithm
https://en.wikipedia.org/wiki/Reservoir_sampling
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        val = self.head.val
        current_node = self.head.next
        count = 1
        while current_node:
            r = random.randint(0, count)
            if r == 0:
                val = current_node.val
            current_node = current_node.next
            count +=1
        return val