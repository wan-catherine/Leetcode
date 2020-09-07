import collections

"""
Sliding windows
Treat the least substring contains all a,b,c as a whole X: 
****X  --> the substring can be : 
    X
   *X
  **X
 ***X
****X

This way it won't duplidated count the number.
"""

class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        start, end = 0, 0
        count = collections.defaultdict(int)
        res = 0
        while end < length:
            count[s[end]] += 1
            while len(count) == 3:
                count[s[start]] -= 1
                if count[s[start]] == 0:
                    del count[s[start]]
                start += 1
            res += start
            end += 1
        return res

