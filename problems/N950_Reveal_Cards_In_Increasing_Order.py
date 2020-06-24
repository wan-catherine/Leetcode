import collections


class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        d = collections.deque()
        for x in sorted(deck)[::-1]:
            d.rotate()
            d.appendleft(x)
        return list(d)