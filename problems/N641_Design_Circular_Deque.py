class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = next

class MyCircularDeque(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self.size = k
        self.current = 0
        self.head = Node(0)
        self.trail = Node(0)
        self.head.next = self.trail
        self.trail.prev = self.head

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        node = Node(value)
        next = self.head.next
        node.next = next
        next.prev = node
        node.prev = self.head
        self.head.next = node
        self.current += 1
        return True

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        node = Node(value)
        prev = self.trail.prev
        prev.next = node
        node.prev = prev
        node.next = self.trail
        self.trail.prev = node
        self.current += 1
        return True

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        next = self.head.next.next
        next.prev = self.head
        self.head.next = next
        self.current -= 1
        return True

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        previous = self.trail.prev.prev
        previous.next = self.trail
        self.trail.prev = previous
        self.current -= 1
        return True

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        else:
            return self.head.next.val

    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        if self.isEmpty():
            return  -1
        else:
            return self.trail.prev.val

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        return self.current == 0

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        return self.current == self.size

# Your MyCircularDeque object will be instantiated and called as such:
obj = MyCircularDeque(3)
print(obj.insertLast(1))
print(obj.insertLast(2))
print(obj.insertFront(3))
print(obj.insertFront(4))
print(obj.getRear())
print(obj.isFull())
print(obj.deleteLast())
print(obj.insertFront(4))
print(obj.getFront())
