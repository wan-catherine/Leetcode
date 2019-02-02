class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.guessTwo(0, n)

        def guessTwo(self, min, max):
            mid = (min + max) // 2
            g = self.guess(mid)
            if g == 0:
                return mid
            elif g == -1:
                return self.guessTwo(min, mid - 1)
            else:
                return self.guessTwo(mid + 1, max)
    def guess(self, num):
        pass