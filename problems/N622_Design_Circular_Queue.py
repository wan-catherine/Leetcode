class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.size = k
        self.arr = [0] * k
        self.start = -1
        self.end = -1
        self.cur = 0

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False

        self.end = (self.end + 1) % (self.size)
        self.arr[self.end] = value
        if self.start == -1:
            self.start += 1
        self.cur += 1
        return True

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.start = (self.start + 1) % (self.size)
        self.cur -= 1
        return True

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.arr[self.start]

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.arr[self.end]

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.cur == 0

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return self.cur == self.size

# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(3)
print(obj.enQueue(1))
print(obj.enQueue(2))
print(obj.enQueue(3))
print(obj.enQueue(4))
print(obj.Rear())
print(obj.isFull())
print(obj.deQueue())
print(obj.enQueue(4))

print(obj.Rear())

