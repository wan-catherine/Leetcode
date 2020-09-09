import collections
"""
Key point:
    For same level, there can't be same letter!!!
    Like AAB : AB, AB this will be the same letter A for the first level.
"""
class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        length = len(tiles)
        counter = collections.Counter(tiles)
        self.res = 0
        for i in range(length):
            self.dfs(i+1, counter)
        return self.res

    def dfs(self, len, counter):
        if len == 0:
            self.res += 1
            return
        for key in counter:
            if counter[key] <= 0:
                continue
            counter[key] -= 1
            self.dfs(len-1, counter)
            counter[key] += 1