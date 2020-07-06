import bisect


class RLEIterator(object):

    def __init__(self, A):
        """
        :type A: List[int]
        """
        self.count = A[::2]
        self.value = A[1::2]
        self.prefix_sum = self.count[:]
        self.used = 0
        for i in range(1, len(self.count)):
            self.prefix_sum[i] += self.prefix_sum[i-1]

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.used += n
        index = bisect.bisect_left(self.prefix_sum, self.used)
        if index == len(self.value):
            return -1
        else:
            return self.value[index]

