class ProductOfNumbers_myself(object):

    def __init__(self):
        self.array = []
        self.prefix_product = [1]
        self.latest_zero_index = -1
        self.count = 0

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.array.append(num)
        self.count += 1
        if not num:
            self.prefix_product.append(0)
            self.latest_zero_index = self.count
        elif self.prefix_product[-1]:
            self.prefix_product.append(self.prefix_product[-1] * num)
        else :
            self.prefix_product.append(num)

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        if self.count - k < self.latest_zero_index:
            return 0
        return self.prefix_product[-1] // self.prefix_product[-k-1] if self.prefix_product[-k-1] else self.prefix_product[-1]

"""
when add a zero, just reset the total array!
"""
class ProductOfNumbers:

    def __init__(self):
        self._arr = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self._arr = [1]
        else:
            self._arr.append(self._arr[-1] * num)

    def getProduct(self, k: int) -> int:
        if len(self._arr) <= k:
            return 0
        else:
            return self._arr[-1] // self._arr[-k - 1]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)