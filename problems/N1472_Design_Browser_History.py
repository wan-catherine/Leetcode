from collections import deque


class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.history = []
        self.history.append(homepage)
        self.cur = 0

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        while len(self.history) > self.cur + 1:
            self.history.pop()
        self.history.append(url)
        self.cur += 1

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        if self.cur - steps >= 0:
            self.cur -= steps
        else:
            self.cur = 0
        return self.history[self.cur]

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        length = len(self.history)
        if self.cur + steps < length:
            self.cur += steps
        else:
            self.cur = length - 1
        return self.history[self.cur]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)