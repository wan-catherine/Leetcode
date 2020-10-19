import random


class Solution(object):

    def __init__(self, n_rows, n_cols):
        """
        :type n_rows: int
        :type n_cols: int
        """
        self.ones = set()
        self.rows, self.cols = n_rows, n_cols
        self.maximum = n_rows * n_cols

    def flip(self):
        """
        :rtype: List[int]
        """
        while True:
            index = random.randint(1, self.maximum)
            if index in self.ones:
                continue
            self.ones.add(index)
            col = index % self.cols
            if not col:
                row = index // self.cols - 1
                col = self.cols - 1
            else:
                row = index // self.cols
                col -= 1
            return [row, col]

    def reset(self):
        """
        :rtype: None
        """
        self.ones.clear()

# Your Solution object will be instantiated and called as such:
# obj = Solution(n_rows, n_cols)
# param_1 = obj.flip()
# obj.reset()