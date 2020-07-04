import bisect


class MyCalendar(object):

    def __init__(self):
        self.events = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if not self.events:
            self.events.append((start,end))
            return True
        index = bisect.bisect(self.events, (start, end))
        length = len(self.events)
        if index - 1 >= 0 and start < self.events[index-1][1]:
            return False
        if index < length and end > self.events[index][0]:
            return False
        bisect.insort(self.events, (start, end))
        return True


