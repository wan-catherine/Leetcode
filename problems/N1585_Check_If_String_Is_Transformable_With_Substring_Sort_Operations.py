import collections

"""
Bubble sorting.
Check c in t , if c in s and there is no c1 < c and index(c1) < index(c), then will be false.
We can bubble a char until it meets some other char which less than it.

Hard part : 
There might contains duplicated numbers . So we need to maintain which number we are really compare at the same time.
"""
class Solution(object):
    def isTransformable(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count_s, count_t = collections.Counter(s), collections.Counter(t)
        if count_s != count_t:
            return False
        positions = [[] for _ in range(10)]
        current = [0] * 10
        for i, c in enumerate(s):
            positions[ord(c) - ord('0')].append(i)

        for c in t:
            index = ord(c) - ord('0')
            for i in range(index):
                if current[i] < len(positions[i]) and positions[i][current[i]] < positions[index][current[index]]:
                    return False
            current[index] += 1
        return True
