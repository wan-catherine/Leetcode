"""
diff array, similar as 1109. Corporate Flight Bookings
"""
class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.arr = []
        self.size = maxSize
        self.offset = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.arr) == self.size:
            return
        self.arr.append(x)
        self.offset.append(0)

    def pop(self):
        """
        :rtype: int
        """
        if not self.arr:
            return -1

        if len(self.offset) > 1:
            self.offset[-2] += self.offset[-1]
        return self.arr.pop() + self.offset.pop()


    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        if not self.arr:
            return
        l = len(self.arr)
        n = l if l <= k else k
        self.offset[n-1] += val
