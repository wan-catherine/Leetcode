class Fancy(object):

    def __init__(self):
        self.arr = []
        self.add = [0]
        self.mul = [1]

    def append(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.arr.append(val)
        self.add.append(self.add[-1])
        self.mul.append(self.mul[-1])

    def addAll(self, inc):
        """
        :type inc: int
        :rtype: None
        """
        self.add[-1] += inc

    def multAll(self, m):
        """
        :type m: int
        :rtype: None
        """
        self.add[-1] *= m
        self.mul[-1] *= m

    def getIndex(self, idx):
        """
        :type idx: int
        :rtype: int
        """
        if idx >= len(self.arr):
            return -1
        m = self.mul[-1] // self.mul[idx]
        inc = self.add[-1] - self.add[idx] * m
        return (self.arr[idx] * m + inc) % (10**9+7)

# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)